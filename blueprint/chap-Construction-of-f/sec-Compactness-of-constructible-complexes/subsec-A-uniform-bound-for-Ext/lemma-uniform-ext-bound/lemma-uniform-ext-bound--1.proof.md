+++
kind = "proof"
of = "lemma-uniform-ext-bound--1"
order = 446003
uses = ["proposition-pro-etale-affines-form-basis", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "definition-weak-contractibility--1", "proposition-left-completeness--1", "corollary-continuity-cohomology--1", "corollary-continuity-cohomology--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-flat-models-generators--1", "lemma-constructible-sheaves--8", "lemma-integral-models--5", "definition-underived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--3", "proposition-comparison-etale-derived-category--5", "lemma-structure-integral-constructible-complexes--3", "proposition-sp-unique-adjoint--1", "lemma-global-lattice-normal-scheme--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
*Reduction to strata.* Bounds pass to extensions in either variable.
Indeed, if $0\to C'\to C\to C''\to0$ is exact, then in the long exact
sequence $\Ext^q(C'',N)\to\Ext^q(C,N)\to\Ext^q(C',N)$ the outer groups
vanish above the larger of the two bounds for $C'$ and $C''$, and so the
middle one does too. Hence a bound that holds for every subquotient of a finite
filtration of the source holds for the source, if we take the maximum.
The same sequence in the second variable shows that a bound that holds
for every subquotient of a finite filtration of the target holds for the
target, with the same value.
In view of Lemma [lemma-constructible-sheaves](3), we may therefore assume
$C=a_!L$, with $a=i\circ u:S\hookrightarrow Z\hookrightarrow X$ as in
Lemma [lemma-sections-support-closed-subscheme] and $L$ lisse. It suffices
to find an integer $d$, depending only on $a$ and $L$, with
$\Ext^q(a_!L,b_!M)=0$ for $q>d$, for all locally closed
$b:T\hookrightarrow X$ and lisse $M$ on $T$. Let
$j:X\setminus Z\hookrightarrow X$ be the open complement of $Z$. When $L$
contains a lisse $\mathcal O_E$-lattice, we show that
$d=\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$ works.

*Lattices.* First take $\Lambda=E$. Since torsion arguments need
integral structures, we choose lattices. After refining the
stratifications (Lemma [lemma-lattices-after-finite-stratification]),
$L$ and $M$ contain lisse $\mathcal O_E$-lattices $L_0$ and $M_0$.
The refinement replaces $a_!L$ and $b_!M$ by
finite extensions of sheaves of the same form, which the first step allows.
The refinement of the source stratum depends only on $L$, and that of the
target only on $M$. So the bound obtained for the refined source strata
is still independent of $N$.

The lattices are locally free of finite rank over $\mathcal O_E$. Indeed,
being lisse, they are locally of the form
$\mathcal O_{E,U}\otimes_{\mathcal O_E}P$ with $P$ finitely generated
(Definition [definition-lisse-sheaves]). As subsheaves of $E$-modules
they are torsion free, so $P$ is free. Lemma [lemma-ext-bound-lattices]
now gives $\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)=0$ for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$.

*Inverting $\pi_E$.* Inverting $\pi_E$ is a filtered colimit. By
continuity of Ext out of $a_!L_0$, the Ext groups over $E$ are therefore
colimits of groups that all vanish in the same range. In detail, we have
$a_!L=a_!L_0[1/\pi_E]$ and
$b_!M=(b_!M_0)[1/\pi_E]=\varinjlim(b_!M_0\xrightarrow{\pi_E}b_!M_0\xrightarrow{\pi_E}\cdots)$.
The adjunction between extension and restriction of scalars gives

$$
R\!\operatorname{Hom}_E\bigl(a_!L,b_!M\bigr)
=R\!\operatorname{Hom}_{\mathcal O_E}\bigl(a_!L_0,(b_!M_0)[1/\pi_E]\bigr).
$$

By Lemma [lemma-continuity-ext-out-constructible-complex](2) the cohomology of
the right side is the colimit of the groups
$\Ext^q_{\mathcal O_E}(a_!L_0,b_!M_0)$. Hence
(5.1) implies the bound for $E$.

*Source:* the proof of Lemma [lemma-uniform-ext-bound].
