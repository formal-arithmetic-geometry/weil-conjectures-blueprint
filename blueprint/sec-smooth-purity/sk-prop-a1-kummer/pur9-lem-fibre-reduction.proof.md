+++
kind = "proof"
of = "pur9-lem-fibre-reduction"
uses = ["pur9-input-strictly-henselian"]
+++
Apply the smooth base change theorem of -thm-smooth-base-changeZZ to the Cartesian square with smooth $C\to\operatorname{Spec}k$ and quasi-compact quasi-separated $S'\to\operatorname{Spec}k$, for the constant sheaf $M$ on $S'$, whose stalks are torsion of order invertible on $k$: it gives $R^qh_{*,\Et,\mathbf Z}M\cong(\text{inverse image to }C\text{ of }H^q(S'_{\Et},M))$, which is $M$ for $q=0$ and $0$ for $q>0$ by Input [pur9-input-strictly-henselian]. Hence the unit $M_C\to Rh_{*,\Et,\mathbf Z}M$ is an isomorphism in $D^+(C_{\Et},\mathbf Z)$, the derived category of abelian sheaves on $C_{\Et}$, and the composition isomorphism of Lemma “Composition of étale derived direct images” (`pur456-pbc-push-composition`, see [sk-thm-sf-comp-composition]) for $C\times_kS'\to C\to\operatorname{Spec}k$ (stated there for $\mathcal O_E/\varpi^n$; the same proof applies to abelian sheaves) identifies $R\Gamma(C\times_kS',M)$ with $R\Gamma(C,M)$ through $h^*$.
