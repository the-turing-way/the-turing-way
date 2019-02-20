
/* fork-example.c */
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
  pid_t pid = fork();
  if (pid == -1) {
    printf("fork failed\n");
    exit(EXIT_FAILURE);
  }

  /* Only reach here if fork succeeded */
  
  if (pid) {
    /* child process */
    /* ... */
    printf("hello from child!\n");
    
  } else {
    /* parent process */
    /* ... */
    printf("hello from parent!\n");
    /* wait for child to finish */
    int status;
    wait(&status);
  }

  return 0;
}
