## Checklist of checklists

The following presents some possible checklists for both the coder and the reviewer, as part of a formal review process.

## Tabke of contents

- [For the coder](#For_the_coder)
- [For the reviewer](#For_the_reviewer)

<a name="For_the_coder"></a>
### For the coder

- [ ] Does the new code meet project standards? In particular,
  - [ ] Is there documentation?
  - [ ] Are there new tests for the new material?
  - [ ] Do these tests pass locally?
  - [ ] Are you following any declared style guides?
  - [ ] Are the tests in the rest of the code base still passing locally?
- [ ] Create the pull request; wait for any CI checks to complete.
- [ ] Consult the CI reports. Did all the builds and tests complete?
- [ ] If necessary, now formally request a review.
- [ ] Once review is complete, discuss any comments necessary.
- [ ] Make the changes, and record the changes made against appropriate comments.
- [ ] Check that the reviewer knows you believe you have fully addressed the review.

<a name="For_the_reviewer"></a>
### For the reviewer

- [ ] Check the code meets basic project style, if this is not automatically checked by CI.
- [ ] Check there are tests & documentation to necessary standards.
- [ ] Read the code, carefully.
  - [ ] Is all the code easily understood? <!-- Chanuki notes that this has been  added to emphaise the importance of readbilty in code-->
  - [ ] Is it clear what all sections of the code do?
  - [ ] Are the logic and approach in the proposed changes clear?
  - [ ] Are the logic and the approach both sound?
  - [ ] Do the tests actually ensure the code is robust in its intended use?
  - [ ] Are there any bugs or other defects?
- [ ] As needed, engage constructively with the coder if they disagree on certain points in order to come to a consensus.
- [ ] Once the coder believes changes are complete, check that they do indeed address all of the initial comments.
- [ ] Approve the changes, and if it is your responsibility, make the merge.
