
/* clone-example.c */
#define _GNU_SOURCE
#include <sys/wait.h>
#include <sys/utsname.h>
#include <sched.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define STACK_SIZE 0x100000 /* 1 Mb */

int child(void *args)
{
  while (1);
}

int main(int argc, char *argv[])
{
  char stack[STACK_SIZE];

  /* stacks are assumed to grow _downwards_ */
  char *stack_top = stack + STACK_SIZE;

  long flags = SIGCHLD /* send SIGCHLD when child returns */
    | CLONE_THREAD     /* run in same thread group */
    | CLONE_SIGHAND    /* share table of signal handlers */
    | CLONE_VM;        /* share virtual memory space */
  
  pid_t pid = clone(child, stack_top, flags, NULL);

  while (1);

  return 0;
}
