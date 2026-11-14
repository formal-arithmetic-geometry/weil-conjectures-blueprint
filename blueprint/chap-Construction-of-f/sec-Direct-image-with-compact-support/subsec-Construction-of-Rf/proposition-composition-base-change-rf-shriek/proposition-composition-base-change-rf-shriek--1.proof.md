+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--1"
order = 516003
uses = ["proposition-pro-etale-affines-form-basis", "definition-lisse-sheaves", "lemma-descent-finite-coefficient-field", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "definition-torsion-sheaves", "proposition-proper-direct-image-constructible-complexes", "proposition-dctf-x-qbar-2-colimit", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-exact-products--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "definition-local-cohomology--1", "lemma-local-cohomology-right-adjoint--1", "definition-derived-adic-completeness--1", "lemma-reduction-derived-nakayama--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--3", "definition-constructible-sheaves--4", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "proposition-integral-constructibility-criterion--1", "proposition-ctf-equals-bc--1", "lemma-constructible-sheaves--3", "lemma-constructible-sheaves--6", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "proposition-proper-direct-image-finite-coefficients--1", "proposition-proper-base-change-complete-integral--1", "proposition-proper-direct-image-constructible-complexes--7", "proposition-proper-direct-image-constructible-complexes--8", "proposition-ind-constructible-sheaves--2", "proposition-ind-constructible-sheaves--3", "proposition-ind-constructible-sheaves--7", "proposition-comparison-etale-derived-category--5", "corollary-proper-direct-image-finite-coefficients-localizing--1", "lemma-proper-direct-image-unbounded-complexes--3", "lemma-structure-integral-constructible-complexes--3", "definition-compactification-refinement--2", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
*The composition isomorphism.* Choose compactifications $f=p\circ j$
and $g=q\circ j_Y$, with $j:X\to\overline X$ and $j_Y:Y\to\overline Y$ open and
$p,q$ proper. In the composite $Rq_*j_{Y!}Rp_*j_!$, the middle factor $j_{Y!}Rp_*$
applies a proper direct image before an extension by zero, and we
want to interchange the two.
Compactify the morphism $j_Y\circ p:\overline X\to\overline Y$ as
$\overline X\xrightarrow{j'}W\xrightarrow{r}\overline Y$, with $j'$ open,
$r$ proper and $\overline X$ dense in $W$. Then $r^{-1}(Y)=\overline X$,
because the open immersion $\overline X\to r^{-1}(Y)$ is a morphism from a proper
$Y$-scheme to a separated $Y$-scheme, hence proper, and its image is
closed, open and dense.

The interchange map is defined as follows. For $M$ in $D(\overline X_{\mathrm{pro}\acute{e}t},\Lambda)$, restriction to the open
$Y\subset\overline Y$ identifies $j_Y^*Rr_*j'_!M$ with $Rp_*M$, because
$r^{-1}(Y)=\overline X$, the restriction of $r$ over $Y$ is $p$, and
$j'_!M$ restricts to $M$ on $\overline X$. By the adjunction $j_{Y!}\dashv j_Y^*$, we obtain a map

$$
j_{Y!}Rp_*M\longrightarrow Rr_*j'_!M,
$$

which is the unique map restricting to the identity of $Rp_*M$ over $Y$.

For $M\in D^b_{\mathrm{ctf}}(\overline X,\Lambda)$, this map is an isomorphism. Over
$Y$ it is the identity, and over $\overline Y\setminus Y$ both sides vanish.
For the right-hand side, the vanishing follows from proper base change on $D^b_{\mathrm{ctf}}$
(Proposition [proposition-proper-base-change-localizing-categories]) for the inclusion
of $\overline Y\setminus Y$ into $\overline Y$, since $j'_!M$ vanishes on
$r^{-1}(\overline Y\setminus Y)=W\setminus\overline X$. Both sides preserve
direct sums on $\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$
(Proposition [proposition-proper-direct-image-extension-zero]). Hence
Lemma [lemma-checking-isomorphisms-constructible-complexes] shows that
(5.9) is an isomorphism for all
$M\in\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$. For $M=j_!K$ it gives

$$
Rq_*j_{Y!}Rp_*j_!K\simeq Rq_*Rr_*j'_!j_!K=R(qr)_*(j'j)_!K,
$$

and the right side is $R(gf)_!K$ computed with the compactification
$gf=(qr)\circ(j'j)$.

*Source:* the proof of Proposition [proposition-composition-base-change-rf-shriek].
