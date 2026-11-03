+++
kind = "proof"
of = "lem-pbc-a3-prime-annihilated-invertible-cases"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Every geometric stalk functor is additive, so applying it to $r\cdot\mathrm{id}_F=0$ shows that every element of every geometric stalk is killed by $r$. If $r$ is a unit in $k$, then $r$ is a common positive annihilator invertible in $k$, as the coefficient condition requires.

If $r$ is not a unit in $k$, then $r=0$ in $k$, so an integer $n$ invertible in $k$ is not divisible by $r$ and is coprime to $r$. By the coefficient condition each stalk element is killed by such an $n$ and also by $r$, hence it is zero. All geometric stalks of $F$ vanish, so the identity of $F$ is zero by conservativity of geometric stalks [lemma-weil-pbc-geometric-stalk-conservative], and $F=0$.
