+++
kind  = "proof"
of    = "lem-sc-sylow-module-filtration"
+++
The intersection of the stabilizers of the finitely many elements
of $M$ is open and normal, by
[def-exc-continuous-cohomology]. Thus the action factors through
a quotient $Q$ of $G$ by an open normal subgroup, which is finite
since $G$ is compact. Choose an $\ell$-Sylow subgroup $P$
of $Q$, and let $H$ be its inverse image. The index $[G:H]$
is prime to $\ell$. First filter $M$ by its powers of $\ell$;
the quotients are finite-dimensional $\mathbf F_\ell[P]$-modules.
Every nonzero such module $V$ has a nonzero invariant vector:
the nontrivial $P$-orbits in its underlying finite set have
cardinality divisible by $\ell$, so
$\#V^P\equiv\#V=0\pmod\ell$. Since $0\in V^P$, this
forces $\#V^P\geq\ell$. The line spanned by a nonzero invariant
vector is a trivial submodule. Induction on $\dim V$, applied
to its quotient by this line, gives the required filtration.
Refining the powers-of-$\ell$ filtration proves the assertion.
