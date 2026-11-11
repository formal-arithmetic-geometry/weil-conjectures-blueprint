+++
kind = "proof"
of = "lemma-uniform-ext-bound--2"
order = 446005
uses = ["proposition-pro-etale-affines-form-basis", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-left-completeness--1", "corollary-continuity-cohomology--1", "corollary-continuity-cohomology--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "proposition-pro-etale-site-separably-closed--3", "lemma-comparison-completed-coefficients--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-inverse-image-coefficient-sheaves--4", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-flat-models-generators--1", "lemma-constructible-sheaves--8", "lemma-integral-models--5", "definition-underived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--3", "proposition-comparison-etale-derived-category--5", "proposition-sp-unique-adjoint--1", "lemma-global-lattice-normal-scheme--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Clause [lemma-uniform-ext-bound--1] establishes the bound over every finite extension, uniformly in that extension.

*The case $\Lambda=\overline{\mathbf Q}_\ell$.* The bound for $E$ depends only on the
strata and on $\operatorname{cd}_\ell$, not on $E$, so it passes to the
colimit over finite extensions. We first fix everything that depends on
$L$ alone, before the target is given. By
Lemma [lemma-descent-lisse-qbar-sheaves-finite], applied to $L$ alone,
there are a finite extension $E_0/\mathbf Q_\ell$ and a lisse $E_0$-sheaf $L'$ with
$L=L'_{\overline{\mathbf Q}_\ell}$. After refining $S$
(Lemma [lemma-lattices-after-finite-stratification]), $L'$ contains a
lisse $\mathcal O_{E_0}$-lattice $L'_0$. As in the case $\Lambda=E$, the
refinement replaces $a_!L$ by a finite extension of sheaves of the same
form, and it depends only on $L$. For every finite extension
$E'\supset E_0$, the sheaf $L'_0\otimes_{\mathcal O_{E_0}}\mathcal O_{E'}$
is a lisse $\mathcal O_{E'}$-lattice in $(L')_{E'}$ on the same strata.
The case $\Lambda=E'$ therefore gives
$\Ext^q_{E'}\bigl((a_!L')_{E'},N'\bigr)=0$ for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$, for each refined
stratum $S$ and every $N'\in\Cons(X,E')$. This bound does not depend on
$E'$ or on $N'$.

Now let $b$ and $M$ be given. By
Lemma [lemma-descent-lisse-qbar-sheaves-finite] again, applied to $M$,
there are a finite extension $E\supset E_0$ (enlarge the field given by the
lemma to contain $E_0$) and a lisse $E$-sheaf $M'$ with $M=M'_{\overline{\mathbf Q}_\ell}$.
The field $E$ depends on $M$, but neither the strata of the source nor the
lattice $L'_0$ do. Then $a_!L=(a_!L')_{\overline{\mathbf Q}_\ell}$ and
$b_!M=(b_!M')_{\overline{\mathbf Q}_\ell}$, and by
Lemma [lemma-descent-finite-coefficient-field](1),

$$
\Ext^q_{\overline{\mathbf Q}_\ell}(a_!L,b_!M)
=\varinjlim_{E'\supset E}\Ext^q_{E'}\bigl((a_!L')_{E'},(b_!M')_{E'}\bigr).
$$

Every group on the right vanishes for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ by the previous
paragraph, and hence so does the colimit.

*Source:* the proof of Lemma [lemma-uniform-ext-bound].
