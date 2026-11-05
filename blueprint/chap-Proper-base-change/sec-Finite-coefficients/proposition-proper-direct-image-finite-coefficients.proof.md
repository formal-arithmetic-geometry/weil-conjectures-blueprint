+++
kind = "proof"
of = "proposition-proper-direct-image-finite-coefficients"
order = 411
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
By Corollary [corollary-finite-tor-amplitude-under-comparison] the
étale and pro-étale categories $D^b_{\mathrm{ctf}}$ agree, and by
Theorem [theorem-comparison-direct-images] so do the proper direct
images of their bounded below complexes. We can therefore transport bounded constructibility and the Tor bound
from the étale site.

On the étale site, let $C\in D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$. The proper
direct image of a constructible torsion sheaf is constructible
[Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0)], and $\operatorname{cd}_\ell(p)<\infty$
[Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)]. Hence $Rp_*C\in\Dbc(Y_{\acute{e}t},A)$.

To check finite Tor amplitude, suppose that $C$ has Tor amplitude $[a,b]$, and let
$d$ be an integer with $\operatorname{cd}_\ell(X_{\bar y})\leq d$ for
all geometric points $\bar y$ of $Y$. Since derived tensor products are computed
stalkwise, it suffices to show that each stalk $(Rp_*C)_{\bar y}$ has
Tor amplitude in $[a,b+d]$ as a complex of $A$-modules. In other words,
$(Rp_*C)_{\bar y}\otimes^{\mathbf L}_AN=((Rp_*C)\otimes_A^{\mathbf L}N_Y)_{\bar y}$
should have cohomology in $[a,b+d]$ for every $A$-module $N$. By proper base change
and the projection formula for constant modules [Stacks, [0F12](https://stacks.math.columbia.edu/tag/0F12)], this stalk is

$$
R\Gamma\bigl(X_{\bar y},
C|_{X_{\bar y}}\otimes_A^{\mathbf L}N_{X_{\bar y}}\bigr).
$$

The complex $C|_{X_{\bar y}}\otimes_A^{\mathbf L}N_{X_{\bar y}}$ has
cohomology in $[a,b]$, because restriction to the fibre preserves Tor
amplitude. Since $R\Gamma(X_{\bar y},-)$ preserves $D^{\geq a}$ and has
cohomological dimension at most $d$, it keeps the lower bound and raises the upper bound by
at most $d$. Thus $Rp_*C\in D^b_{\mathrm{ctf}}(Y_{\acute{e}t},A)$, with Tor amplitude in $[a,b+d]$.
