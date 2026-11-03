+++
kind = "proof"
of = "lem-pbc-a3-prime-annihilated-primary-cases"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Every geometric stalk functor is additive, so applying it to $r\cdot\mathrm{id}_F=0$ shows that every element of every geometric stalk is killed by $r$; exponent one proves that $F$ is $r$-primary.

If $p\ne r$ is a prime and $F$ is $p$-primary, every stalk element is killed by some $p^n$ and by $r$, which are coprime, so it is zero. All geometric stalks vanish, so the identity of $F$ is zero by conservativity of geometric stalks [lemma-weil-pbc-geometric-stalk-conservative], and $F$ is a zero object.
