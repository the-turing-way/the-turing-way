<a name="Summary_of_ways_to_capture_computational_environments"></a>

## Summary of ways to capture computational environments

There are a number of ways of capturing computational environments. The major ones covered in this chapter will be package management systems, Binder, virtual machines, and containers. Each have their own pros and cons, and which is the most appropriate for you will depend on the nature of your project.

These can be broadly split into two categories: those that capture only the software and its versions used in an environment (package management systems), and those that replicate an entire computational environment including the operating system and customised settings (virtual machines and containers).

Another way these can be split is by how the reproduced research is presented to the reproducer. Using Binder or a virtual machine creates a much more graphical, GUI-type result, whereas the outputs of containers and package management systems are more easily interacted with via the command line.

<table>
  <tr>
    <th></th>
    <th></th>
    <th colspan="2">Interaction style</th>
  </tr>
  <tr>
  <th></th>
  	<td></td>
    <td>Graphical</td>
    <td>Command line</td>
  </tr>
  <tr>
    <th rowspan="2">What is reproduced?</th>
    <td>Software and versions</td>
    <th>Binder</th>
    <th>Conda</th>
  </tr>
  <td>Entire system</td>    
  <th>Virtual Machines</th>
  <th>Containers</th>  
  <tr>
  </tr>
</table>

Here we give a brief description of each of these tools:

<a name="Package_management_systems_outline"></a>

### Package management systems

Package management systems are tools used to install and keep track of the software (and critically versions of software) used on a system, and can export files specifying these required software packages/versions. The files can be shared with others who can use them to replicate the environment, either manually or via their own package management systems.

<a name="Binder_outline"></a>

### Binder

Binder is a service which generates fully-functioning versions of projects from a git repository and serves them on the cloud. These "binderized" projects can be accessed and interacted with by others via a web browser. In order to do this Binder requires that the software (and optionally versions) required to run the project are specified. Users can make use of package management systems or Dockerfiles (discussed in the [Containers section](#Containers_section)) to do this if they so desire.

<a name="Virtual_machines_outline"></a>

### Virtual machines

Virtual machines are simulated computers. A user can make a "virtual" computer very easily, specifying the operating system they want it to have among other features, and run it like any other app. Within the app will be the desktop, file system, default software libraries and other features of the specified machine, which can be interacted with as if it was a real computer. Virtual machines can be easily replicated and shared. This allows researchers to create virtual machines, perform their research on them, and then save their state along with their files, settings and outputs, which they can then distribute as a fully-functioning project.

<a name="Containers_outline"></a>

### Containers

Containers offer many of the same benefits as virtual machines. They essentially act as entirely separate machines which can contain their own files, software and settings.

The difference is that virtual machines include an entire operating system along with all the associated software. that is typically packaged with it- regardless of whether the project actually makes use of that associated software. Containers only contain the software and files explicitly defined within them in order to run the project they contain. This makes them far more lightweight than virtual machines.

Containers are particularly useful if projects need to be able to run on high performance computing environments as, since they already _contain_ all the necessary software, they save having to install anything on an unfamiliar system where the researcher may not have the required permissions to do so.
