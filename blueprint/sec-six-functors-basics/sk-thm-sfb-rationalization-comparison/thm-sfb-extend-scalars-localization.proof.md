+++
kind  = "proof"
of    = "thm-sfb-extend-scalars-localization"
uses = ["lem-sfb-extend-scalars-bounded-constructible", "sk-def-sfb-derived-extension-of-scalars"]
+++
Write $F=E\otimes^{\mathrm L}_{\cO_E}-$, $\mathcal T=D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)$
and $\mathcal T'=D_{\mathrm{cons}}(X_{\mathrm{proét}},E)$. By the proof of
[lem-sfb-extend-scalars-bounded-constructible], $F$ is induced by the exact functor
$E_X\otimes_{\cO_{E,X}}-$ with $E_X=\colim(\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\to\cdots)$.
So $F$ is triangulated.

*$F$ inverts $W_{\ell^{\mathbf N}}$.* If $\ell^n\cdot\mathrm{id}_Z=0$, then
$\ell^n\cdot\mathrm{id}_{F(Z)}=0$. But $\ell$ acts invertibly on $E_X$-modules, so
$F(Z)=0$. A morphism with $\ell$-power-torsion cone is therefore sent to a morphism with
zero cone, i.e. to an isomorphism. So $F$ factors through
$\bar F\colon\mathcal T[\ell^{-1}]\to\mathcal T'$.

*Morphisms of the rationalization.* For $s\colon L\to L'$ in $W_{\ell^{\mathbf N}}$ with
cone $C$ killed by $\ell^n$, the composite $L'\to C$ of $\ell^n\cdot\mathrm{id}_{L'}$ is
zero. So $\ell^n\cdot\mathrm{id}_{L'}=s\circ t$ for some $t\colon L'\to L$. Then
$s\circ(t\circ s-\ell^n)=0$, so $t\circ s-\ell^n$ factors through $C[-1]$ and is killed by
$\ell^n$, which gives $(\ell^nt)\circ s=\ell^{2n}$. Hence the multiplications by $\ell^n$
are cofinal in $W_{\ell^{\mathbf N}}$, and
$$
\Hom_{\mathcal T[\ell^{-1}]}(K,L)=\colim\bigl(\Hom_{\mathcal T}(K,L)\xrightarrow{\ell}\Hom_{\mathcal T}(K,L)\xrightarrow{\ell}\cdots\bigr)=\Hom_{\mathcal T}(K,L)[\ell^{-1}].
$$

*Full faithfulness of $\bar F$.* By the adjunction
$F\dashv D(\operatorname{Res}_\varphi)$ [sk-def-sfb-derived-extension-of-scalars],
$\Hom_{\mathcal T'}(F(K),F(L))=\Hom(K,E_X\otimes_{\cO_{E,X}}L)$, and
$E_X\otimes_{\cO_{E,X}}L$ is the sequential homotopy colimit of $L\xrightarrow{\ell}L\to\cdots$.
So full faithfulness amounts to the commutation
$$
\colim_\ell\Hom(K,L)\xrightarrow{\ \sim\ }\Hom(K,\colim_\ell L)
$$
for bounded constructible $K,L$. By dévissage along the canonical truncations and the
common stratification of the proof of [sk-def-sfb-bounded-constructible], one reduces to
$K$ a single locally finitely presented module on a stratum. There $\Hom(K,-)$ is
computed by pro-étale cohomology on a quasi-compact quasi-separated scheme (a
topologically Noetherian scheme is such), which commutes with filtered colimits
(Bhatt–Scholze, §6.8).

*Essential surjectivity.* The essential image of the fully faithful triangulated functor
$\bar F$ is closed under extensions and shifts. Every object of $\mathcal T'$ is an
iterated extension of shifts of its constructible cohomology sheaves. So it suffices that
every constructible $E_X$-module is $E_X\otimes N$ for a bounded constructible
$\cO_{E,X}$-complex $N$. This is the existence of $\cO_E$-lattices: scale a local
presentation by a power of $\ell$ to make it integral, and glue over the finitely many
strata and a finite subcover (Bhatt–Scholze, §6.8).

So $\bar F$ is an equivalence, i.e. $F$ is a localization at $W_{\ell^{\mathbf N}}$.
