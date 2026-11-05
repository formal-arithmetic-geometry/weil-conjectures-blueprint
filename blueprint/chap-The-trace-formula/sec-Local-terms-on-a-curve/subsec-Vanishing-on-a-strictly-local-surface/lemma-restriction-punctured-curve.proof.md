+++
kind = "proof"
of = "lemma-restriction-punctured-curve"
order = 977
uses = ["lemma-acyclic-resolutions", "lemma-cohomology-near-two-transverse-divisors", "lemma-schematic-closure-uniqueness"]
+++
The source is $R\Gamma(X-D_2,j'_!N)=R\Gamma(X,M)$, by the definition
$M=Rj_*j'_!N$. Since $C$ meets $D_2$ only at $w$, the punctured curve
$C_{(w)}-w$ lies over the strict localization of $X$ at $w$ and avoids
$D_2$. The map therefore factors as the
restriction to $R\Gamma(D_2,M|_{D_2})$, followed by the
restriction to the stalk $M_w=R\Gamma(X_{(w)}-D_2,j'_!N)$ (by the stalk formula), followed
by the restriction to the displayed target. Since all these maps are restrictions of the same complex, the composite is the given map.
If $w\ne z$, the middle map is zero by Lemma [lemma-cohomology-near-two-transverse-divisors].
If $w=z$, the intermediate object $M_z$ is zero.
