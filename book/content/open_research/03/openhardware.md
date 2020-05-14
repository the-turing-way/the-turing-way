## Open hardware

"Open hardware", or "open source hardware", refers to the design specifications of a physical object that are licenced in such a way that said object can be studied, modified, created, and distributed by anyone.
Like open source software, the "source code" for open hardware - schematics, blueprints, logic designs, Computer Aided Design (CAD) drawings or files, and the like, is available for modification or enhancement by anyone.
Users with access to the tools that can read and manipulate these source files can update and improve the physical device and the code that underlies it, and, if they wish, proceed to share such modifications.

Open hardware's source code should be readily accessible, and its components are preferably easy for anyone to obtain.
Essentially, open hardware eliminates common roadblocks to the design and manufacture of physical goods; it provides as many people as possible the ability to construct, remix, and share their knowledge of hardware design and function.

It is worth noting that open hardware does not necessary mean free. Units may still be sold (by the original designer or by others), but users *could* build them from scratch. Whether or not they choose to buy the unit, users can still get a full understanding of how the hardware works from open documentation, designs, and similar.  

### Why open hardware?

Open hardware allows researchers to understand exactly what their equipment is doing, how it is doing it, and to verify that it is doing it correctly, rather than having to extend a degree of trust.
Being aware of how the equipment that generates a result works puts researchers on a firmer footing in assessing those results.
Open hardware also makes research more reproducible as researchers looking to verify results can do the same thing.

Other benefits of open hardware include protection against lock-in.
Proprietary software for core infrastructure increases the risk of becoming locked in by the vendor or technology.
If this happens, researchers can be at the mercy of vendors' price increases and experience a lack of flexibility they can not easily and readily escape.
Further, if researchers want to modify their equipment to better suit their needs it is much easier to do so (and may only be legal) in the case of open source hardware.

### Elements of an open source hardware project

Here are some files that you should consider sharing when publishing your open source hardware project.
You are not required to post them all, but the more you share the more the community benefits.
There is a lot of crossover here with files to include in open source software projects.

#### Overview and introduction
Your open source hardware project should include a general description of the hardware's identity and purpose, written as much as possible for a general audience.
That is, explain what the project is and what it is for before you get into the technical details.

#### A licence
An appropriate license on the Open Hardware project and its content grant legal permission to anyone to re-use, modify and distribute the different components of a project according to the terms stated (for example, they must acknowledge your contribution).  

#### Original design files
These are the original source files that you would use to make modifications to the hardware's design.
The act of sharing these files is the core practice of open source hardware.
- Ideally, your open source hardware project would be designed using a free and open source software application, to maximize the ability of others to view and edit it.
For better or worse, hardware design files are often created in proprietary programs and stored in proprietary formats.
It is still essential to share these original design files; they constitute the original "source code" for the hardware.
They are the very files that someone will need in order to contribute changes to a given design.
- Try to make your design files easy for someone else to understand. In particular, organize them in a logical way, comment complex aspects, and note any unusual manufacturing procedures.
- Examples of Original Design Files include 2D drawings and computer-aided design (CAD) files.

#### Auxiliary design files
Beyond the original design files, it is often helpful to share your design in additional, more accessible formats.
For example, best practice open sourcing a CAD design is to share the design not just in its native file format, but also in a range of interchange and export formats that can be opened or imported by other CAD programs.
- It is also helpful to provide ready-to-view outputs that can easily be viewed by end-users who wish to understand (but not necessarily modify) the design.
For example, a PDF of a circuit board schematic.
These auxiliary design files allow people to study the design of the hardware, and sometimes even fabricate it, even without access to particular proprietary software packages.
However, note that auxiliary design files are never recommended as substitutes for original design files.

#### Additional technical drawings
In their original formats, if required for fabrication of the device, in a commonly-readable format such as PDF.

#### Bill of materials
While it might be possible to infer from the design files which parts make up a piece of hardware, it is important to provide a separate bill of materials.
This can be a spreadsheet (for example, CSV, XLS, Google Doc) or simply a text file with one part per line.
Useful things to include in the bill of materials are part numbers, suppliers, costs, and a short description of each part.
Make it easy to tell which item in the bill of materials corresponds to which component in your design files: use matching reference designators in both places, provide a diagram indicating which part goes where, or otherwise explain the correspondence.

#### Software and firmware
You should share any code or firmware required to operate your hardware.
This will allow others to use it with their hardware or modify it along with their modifications to your hardware.
Document the process required to build your software, including links to any dependencies (for example, third-party libraries or tools). In addition, it is helpful to provide an overview of the state of the software (for example, "stable" or "beta" or "barely-working hack").

#### Photos
Photos help people understand what your project is and how to put it together.
It is good to publish photographs from multiple viewpoints and at various stages of assembly. If you do not have photos, posting 3D renderings of your design is a good alternative. Either way, it is good to provide captions or text that explain what is shown in each image and why it is useful.

#### Instructions and other explanations
In addition to the design files themselves, there are a variety of explanations that are invaluable in helping others to make or modify your hardware:
- Making the hardware: To help others make and modify your hardware design, you should provide instructions for going from your design files to the working physical hardware.
As part of the instructions, it is helpful to link to datasheets for the components/parts of your hardware and to list the tools required to assemble it.
If the design requires specialized tools, tell people where to get them.
- Using the hardware: Once someone has made the hardware, they need to know how to use it.
Provide instructions that explain what it does, how to set it up, and how to interact with it.
- Design rationale: If someone wants to modify your design, they will want to know why it is the way it is.
Explain the overall plan of the hardware's design and why you made the specific choices you did.
- Limit jargon: Keep in mind that these instructions may be read by someone whose expertise or training is different from yours.
As much as possible, try to write to a general audience, check your instructions for industry jargon, and be explicit about what you assume the user knows.
- Format: The instructions could be in a variety of formats, such as a wiki, text file, Google Doc, or PDF.
Remember, though, that others might want to modify your instructions as they modify your hardware design, so it is good to provide the original editable files for your documentation, not just output formats like PDF.

### Open source hardware processes and practices

#### Designing your hardware

If you are planning to open source a particular piece of hardware, following certain best practices in its design will make it easier for others to make and modify the hardware:

- Use free and open source software design (CAD) tools where possible: If that is not feasible, try to use low-cost and/or widely-used software packages.
- Use standard and widely-available components, materials, and production processes: Try to avoid parts that are not available to individual customers or processes that require expensive setup costs.

#### Hosting your design files

A basic way of sharing your files is with a zip file on your website.
While this is a great start, it makes it difficult for others to follow your progress or to contribute improvements.
Using an online source-code repository (like GitHub, GitLab, or NotaBug) may be a better place to store your open source hardware projects.

#### Distributing open source hardware

- Provide links to the source (original design files) for your hardware on the product itself, its packaging, or its documentation.
- Make it easy to find the source (original design files) from the website for a product.
- Label the hardware with a version number or release date so that people can match the physical object with the corresponding version of its design files.
- In general, clearly indicate which parts of a product are open source (and which are not).
