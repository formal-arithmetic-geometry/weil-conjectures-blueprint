+++
kind = "proof"
of = "theorem-proper-base-change-classical-pro"
order = 404
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "lemma-identity-pasting", "proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
We work on the étale site, where Propositions [proposition-proper-base-change-projective-line]
and [proposition-proper-base-change-etale-site] apply to the torsion rings
$\Lambda/p\Lambda$. By dévissage we reach all [torsion](@definition-torsion-sheaves) sheaves of
$\Lambda$-modules, and the comparison theorems then bring us back to the
[pro-étale site](@definition-small-pro-etale-site).

By Corollary [corollary-bounded-below-classical-complexes], we may write $K=\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K_{\acute{e}t}}$
with $K_{\acute{e}t}\in D^+(X_{\acute{e}t},\Lambda)$, and the cohomology sheaves of $K_{\acute{e}t}$
are [torsion](@definition-torsion-sheaves). Indeed, [$\nu_X^*$](@proposition-comparison-morphism-inverse-image) is exact, commutes with colimits and is fully
faithful on sheaves, and therefore detects the condition $F=\varinjlim_nF[n]$
of Definition [definition-torsion-sheaves]. We must show that the [base change
map](@definition-derived-base-change-map) for $K_{\acute{e}t}$ is an isomorphism in $D^+(Y'_{\acute{e}t},\Lambda)$, and then
pass to the [pro-étale site](@definition-small-pro-etale-site).

We reduce to the rings $\Lambda/p\Lambda$, $p$ prime. These are killed by
$p$, so [$\mathrm{PBC}_{\Lambda/p\Lambda}(f)$](@definition-torsion-pbc-property) holds by
Propositions [proposition-proper-base-change-projective-line] and [proposition-proper-base-change-etale-site]. Now a sheaf $F$ of
$\Lambda$-modules with $pF=0$ is a sheaf of $\Lambda/p\Lambda$-modules, and
restriction of scalars along $\Lambda\to\Lambda/p\Lambda$ is exact and
conservative. Moreover, it commutes with inverse images, derived direct images
and [base change maps](@definition-derived-base-change-map), since both derived direct images are computed on
underlying abelian sheaves
(Lemma [lemma-cohomology-modules-underlying-abelian]). Hence the [base change map](@definition-derived-base-change-map) for $F$ is an
isomorphism.

If $nF=0$, we argue by induction on the number of prime
factors of $n$. For a prime $p\mid n$, the outer terms of
$0\to \href{@definition-torsion-sheaves}{F[p]}\to F\xrightarrow{p}pF\to0$ are killed by $p$ and by $n/p$,
so the five lemma applies to the long exact cohomology sequences. Finally, a [torsion](@definition-torsion-sheaves)
sheaf is the filtered colimit $\varinjlim_n\href{@definition-torsion-sheaves}{F[n]}$. Since
(4.7) applies to the qcqs morphisms $f$ and $f'$,
the [base change map](@definition-derived-base-change-map) is an isomorphism for every [torsion](@definition-torsion-sheaves) sheaf of
$\Lambda$-modules. The truncation argument at the end of the proof of
Theorem [theorem-pbc-injective-acyclicity] then passes from sheaves to bounded below complexes with
[torsion](@definition-torsion-sheaves) cohomology, in particular to $K_{\acute{e}t}$.

To return to the [pro-étale site](@definition-small-pro-etale-site) we apply [$\nu_{Y'}^*$](@proposition-comparison-morphism-inverse-image). Since $f$ and
$f'$ are proper, hence qcqs, the comparison of direct images in
Theorem [theorem-comparison-direct-images] applies. Using it together with the
comparison of inverse images $\href{@proposition-topos-functoriality}{g_{\mathrm{pro}\acute{e}t}^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}\simeq\href{@proposition-comparison-morphism-inverse-image}{\nu_{Y'}^*}g_{\acute{e}t}^*$, we
identify [$\nu_{Y'}^*g^*Rf_*K_{\acute{e}t}$](@proposition-comparison-morphism-inverse-image) and
[$\nu_{Y'}^*Rf'_*g'^*K_{\acute{e}t}$](@proposition-comparison-morphism-inverse-image) with $g^*Rf_*K$ and $Rf'_*g'^*K$ in
$D^+(\href{@definition-small-pro-etale-site}{Y'_{\mathrm{pro}\acute{e}t}},\Lambda)$. By the last assertion of
Lemma [lemma-naturality-pasting-comparison], under these identifications the
[base change map](@definition-pro-etale-base-change-map) of $K$ is the inverse image on [$Y'_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site) of the étale
[base change map](@definition-derived-base-change-map) of $K_{\acute{e}t}$. We have shown that the latter is an isomorphism.
