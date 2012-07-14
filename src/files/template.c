unsigned char shellcode[] = "PUTSHELLCODEHERE";

int  main()
{
      // Function pointer points to the address of function.
      void (*shell)(); //Function pointer
      // Initializing a function pointer  with the address of a shellocde
      // & is optional
      shell= &shellcode;
      // Execute shellcode
      shell();
      return 0;
}
