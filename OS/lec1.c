// we can represent system calls like regular C functions

//by convention, therare some expected file descriptors
// 0-standard input, 1-standard output, 2-standard error

//the most basic helloworld program
void _start(void){
    write(1, "Hello world!\n", 12);
    exit_group (0);
}

//API tells you what and ABI tells you how
//ABI specifies the details, specifically how to pass arguments and where the return value is 

//generate an interrupt with a svc instruction

//out bytes represemt an elf file
//elf file is a binary file that contains the code and data for a program
//file header contains metadata about the file
//program header table contains information about the segments

//system calls transition between user and kernal mmode

//kernal interfaces operate between cpu ode boundries


//the kernal is the part of the os that interacts with hardware
//systems calls are the interface btetween user and kernal mode
//file format and instructions to define simple hellow world in 168bytes
//different kernal architectures shift how much code runs in kernal mode