+++
kind  = "proof"
of    = "det-prop-sf-cbc"
uses = ["thm-cbc-finite-torsion", "thm-cbc-finite-level-proetale", "det-def-sfb-shriek-base-change-morphism", "det-thm-sfb-shriek-base-change", "thm-cbc-complete-proetale"]
+++
The stages are proved separately. For finite coefficients on the étale site,
choose a compactification $f=rj$ with $j$ an open immersion and $r$ proper,
and base change it to a compactification $f'=r'j'$ of $f'$. Then
$\operatorname{Ex}_!$ is the exchange map computed with these
compactifications, followed by the comparison isomorphism identifying the
functor $Rr'_*j'_!$ with $Rf'_!$. The exchange for $j_!$ is an isomorphism
because extension by zero commutes with every base change, so the computed
exchange reduces to the base-change map $Lg^*Rr_*\to Rr'_*Lg''^*$ for the
proper morphism $r:Z\to Y$, where $g'':Z'=Z\times_YY'\to Z$ is the projection, which is an isomorphism on $D^+$ by proper base
change with torsion coefficients ([thm-cbc-finite-torsion]). The remaining
stages are: the pro-étale site at finite $\Lambda$, for objects with an
étale-origin witness, transported from the étale case
([thm-cbc-finite-level-proetale]); and the condensed categories
$\Dbc(X,\Lambda)$ for $\Lambda=\mathcal O_E,E,\Qlb$, where
$\operatorname{Ex}_!$ is the morphism of
[det-def-sfb-shriek-base-change-morphism] and is an isomorphism by
[det-thm-sfb-shriek-base-change] at $E,\Qlb$ and by
[thm-cbc-complete-proetale] at $\mathcal O_E$.
