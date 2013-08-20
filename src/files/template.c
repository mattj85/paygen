unsigned char shellcode[] = "PUTSHELLCODEHERE";

int  main()
{
      void (*shell)(); //Function pointer
      shell= &shellcode;
      shell();
      return 0;
}
