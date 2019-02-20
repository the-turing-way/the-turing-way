
#define _GNU_SOURCE
#include <stdio.h>
#include <sys/wait.h>
#include <sys/utsname.h>
#include <sched.h>
#include <linux/sched.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <dirent.h>
#include <sys/mount.h>
#include <limits.h>

#define STACK_SIZE 0x100000 /* 1 Mb */

int child(void *args)
{
  /* set container root */
  const char *container_root = "absolute path to container root";
 
  /* chroot to container root */
    if (chroot(container_root)) {
      printf("Could not chroot, reason: %s", strerror(errno));
      exit(EXIT_FAILURE);
    }
    chdir("/");

  /* mount sys and proc */
  mount("proc", "proc", "proc", 0L, "");
  mount("sys", "sys", "sys", 0L, "");

  /* exec the requested command */
    char **envp = {NULL};
    if (execve(argv[0], argv, envp)) {
      printf("Failed to exec, reason: %s", strerror(errno));
      exit(EXIT_FAILURE);
    }

  return 0;
}

int main(int argc, char **argv) {
  char stack[STACK_SIZE];
  char *stack_top = stack + STACK_SIZE;

  /* set flags to pass to clone */
    int flags = SIGCHLD
      | CLONE_NEWPID
      | CLONE_NEWUTS
      | CLONE_NEWIPC
      | CLONE_NEWUSER
      | CLONE_NEWNET
      | CLONE_NEWNS;

  /* call clone */
    pid_t pid = clone(child, stack_top, flags, argv + 1);
    if (pid == -1) {
      printf("clone failed\n");
      exit(EXIT_FAILURE);
    }

  /* set container users and groups */
  char path[PATH_MAX];
  
  sprintf(path, "/proc/%d/uid_map", pid);
  FILE *file = fopen(path, "w");
  fprintf(file, "%d %d %d", 0, getuid(), 1);
  fclose(file);
  
  sprintf(path, "/proc/%d/setgroups", pid);
  file = fopen(path, "w");
  fprintf(file, "deny\n");
  fclose(file);
  
  sprintf(path, "/proc/%d/gid_map", pid);
  file = fopen(path, "w");
  fprintf(file, "%d %d %d", 0, getgid(), 1);
  fclose(file);

  int status;
  wait(&status);
 
  return 0;
}
