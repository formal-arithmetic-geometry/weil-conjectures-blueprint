+++
kind = "proof"
of = "lemma-lattices-lisse-e-sheaves--1"
order = 260001
uses = ["proposition-pro-etale-coverings", "lemma-stability", "lemma-comparison-completed-coefficients"]
+++
Identify the continuous coefficient sheaves with those obtained from the
extended $\ell$-adic absolute value. Consider pairs consisting of a locally
free integral module of finite rank and an isomorphism from its scalar
extension to $L$. Two pairs are equivalent when an integral isomorphism
intertwines their scalar-extension isomorphisms. Their classes form a sheaf:
each pair embeds in $L$, equivalent pairs have the same image, and matching
images glue by descent of module sheaves.

On a trivializing object where $L$ has rank $r$, this sheaf is the constant
sheaf on

$$
\GL_r(E)/\GL_r(\mathcal O_E).
$$

Indeed, a constant matrix gives an integral lattice. A local integral basis
gives a continuous change-of-basis matrix, and the openness of
$\GL_r(\mathcal O_E)$ makes its coset locally constant. This identifies the
constant coset sheaf with the sheaf of classes. The identity coset supplies
a section on each trivializing object, also when $r=0$.

The classes inject into the set of families of their embedded submodules
on the slice site. Replace the section sets by sets of the required size
through these injections and transport the restriction maps and sheaf
condition. The equivalence between the slice site and the covering member's
small pro-étale site transports the constant descriptions. Finally, choose
a representative of a class whenever the section set is nonempty and
transport its integral module and scalar-extension isomorphism back along
the coefficient identifications. For the empty scheme the empty covering
suffices.
