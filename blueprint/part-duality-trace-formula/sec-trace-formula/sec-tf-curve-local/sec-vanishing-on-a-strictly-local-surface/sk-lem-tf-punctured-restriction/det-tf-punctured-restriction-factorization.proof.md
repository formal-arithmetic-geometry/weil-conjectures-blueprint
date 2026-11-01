+++
kind = "proof"
of = "det-tf-punctured-restriction-factorization"
+++
*The maps are defined.* $R\Gamma(Z,Rj_*F)=R\Gamma(Z-Y,F)$ because
$R\Gamma(Z,-)\circ Rj_*=R\Gamma(Z-Y,-)$. Since $s\in Y$, the stalk
of $M|_Y$ at $s$ is $M_s$. The stalk
formula for an open direct image
([Stacks, Tag 03Q7](https://stacks.math.columbia.edu/tag/03Q7)), whose
hypotheses ($j$ quasi-compact and quasi-separated, $F\in D^+$) hold, with
the commutation of cohomology with the limit of étale neighbourhoods,
gives $M_s=R\Gamma(Z_{(s)}-Y,F)$, where $Z_{(s)}-Y$ is the inverse image
of $Z-Y$ in $Z_{(s)}$. The strict localization $C_{(s)}$ maps to
$Z_{(s)}$, and since $C\cap Y=\{s\}$ set-theoretically, $C_{(s)}-s$ maps
into $Z_{(s)}-Y$; this map composed with $Z_{(s)}-Y\to Z-Y$ is $\iota$.

*The composite.* Each of the three maps is a pullback map on
cohomology, along $Y\to Z$, along the geometric point
$s\to Y$ (realized as the limit of étale neighbourhoods), and along
$C_{(s)}-s\to Z_{(s)}-Y$. Pullback maps on cohomology are compatible
with composition, and the first two together are the pullback of
$R\Gamma(Z,M)$ to the stalk $M_s$ along $s\to Z$. Under the
identifications above all of them are restrictions of sections of the
same complex $F$ from $Z-Y$ to schemes over $Z-Y$, so their composite is
the restriction along $\iota$. The last assertion is immediate.
