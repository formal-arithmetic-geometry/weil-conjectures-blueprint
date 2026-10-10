+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-pullback-descent"
uses = ["lemma-weil-pbc-finite-pullback-closed-fibre"]
+++
The equality $u^\sharp(x)=x'$ is the descent witness. Applying $a^\sharp$ to it
gives $a^\sharp(x')=a^\sharp(u^\sharp(x))$, and the right-hand side equals
$\Gamma(\theta)(b^\sharp(i^\sharp(x)))$ by
[lemma-weil-pbc-finite-pullback-closed-fibre]. The composition lemma
[lemma-weil-pbc-finite-pullback-composition] is what that equation rests on.
