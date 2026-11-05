+++
kind = "proof"
of = "proposition-ell-adic-cycle-class-diagonal"
order = 602
+++
The cycle class comes from a single map defined with
$\mathbf Z$-coefficients, the boundary of the divisor sequence. Hence all
its reductions are reductions of one map of systems.

The diagonal is an effective Cartier divisor, which gives a boundary
morphism $\Delta_*\mathbf Z\to\mathbf G_m[1]$ (Lemma [lemma-cycle-class-cartier-divisor]).
Tensoring with the system $(\mathbf Z/\ell^n)_n$ and using the Kummer
sequence, we get one morphism of systems
$\Delta_*\mathbf Z/\ell^\bullet\to\mathbf Z/\ell^\bullet(1)[2]$. Its level
$n$ is the class of Lemma [lemma-cycle-class-cartier-divisor] for
$\mathbf Z/\ell^n$. The transition maps between levels are part of
the data, and this is what a family of separately constructed
classes would lack. Next we take $R\varprojlim$. The site is replete with
exact products
(Propositions [proposition-repleteness-pro-etale-topos] and [proposition-exact-products]).
Hence $R\varprojlim\circ(-\otimes\mathbf Z/\ell^\bullet)$ is derived
$\ell$-completion [Stacks, [099M](https://stacks.math.columbia.edu/tag/099M)], and the limit $\Delta_*\mathbf Z_\ell\to\mathbf Z_\ell(1)[2]$
is the completion of the boundary map of
Lemma [lemma-cycle-class-cartier-divisor]. It is linear over the
completed coefficient sheaf by [Stacks, [099I](https://stacks.math.columbia.edu/tag/099I)]. We obtain the trace in the
same way from the decomposition of $Rq_*\mathbf Z/\ell^\bullet$.

Each $\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta)$ is an endomorphism of
$\mathbf Z/\ell^\bullet$ in degree $0$, that is, a family of endomorphisms
of the levels. These are the identity by
Proposition [proposition-adjunction-projective-line]. We then extend
scalars to $\mathcal O_E$, invert $\ell$ and take the colimit over finite
extensions (Corollary [corollary-continuity-cohomology]). Base change holds
because the Cartier and Kummer maps are natural and pullback commutes with
$R\varprojlim$ here (Lemma [lemma-inverse-image-coefficient-sheaves]).
