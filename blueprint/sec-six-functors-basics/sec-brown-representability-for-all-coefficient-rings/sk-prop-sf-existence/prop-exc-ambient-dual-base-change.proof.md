+++
kind  = "proof"
of    = "prop-exc-ambient-dual-base-change"
+++
Compact-support base change is the isomorphism
$Lg^*Rf_!\xrightarrow{\sim}Rf'_!Lg'^*$ of
[def-cbc-exchange-map]. By
[def-weil-ambient-exceptional-adjoint] the functors $Rf_!$ and
$Rf'_!$ have the right adjoints $Rf^{\times}$ and $Rf'^{\times}$;
the right adjoint of the composite $Lg^*Rf_!$ is the composite
$Rf^{\times}Rg_*$ of the right adjoints, and the right adjoint of
$Rf'_!Lg'^*$ is $Rg'_*Rf'^{\times}$. An isomorphism of functors
induces, by uniqueness of right adjoints, a unique isomorphism of their
right adjoints compatible with the units and counits; applied to the
displayed compact-support base change this is $\beta^{\vee}$.

On the coefficient class the same argument runs object-wise with the
relative adjunctions of [thm-sf-ambient-adjoint-class]. Let $L$ be
bounded below on $Y'$ and let $K$ be a bounded-below object of étale
origin on $X$. Then $Rg_*L$ is bounded below, and $Lg'^*K$ is bounded
below and of étale origin by [lem-weil-pbc-comparison-pullback], so the
bijections

$$
\begin{aligned}
\operatorname{Hom}(K,Rf^{\times}Rg_*L)&\cong\operatorname{Hom}(Rf_!K,Rg_*L)
\cong\operatorname{Hom}(Lg^*Rf_!K,L)\\
&\cong\operatorname{Hom}(Rf'_!Lg'^*K,L)
\cong\operatorname{Hom}(Lg'^*K,Rf'^{\times}L)
\cong\operatorname{Hom}(K,Rg'_*Rf'^{\times}L)
\end{aligned}
$$

are defined, natural in $K$, and given by composition with
$\beta^{\vee}_L$. Both $Rf^{\times}Rg_*L=\nu_X^*f^{\times}R\nu_{Y,*}Rg_*L$ and
$Rg'_*Rf'^{\times}L=Rg'_*\nu_{X'}^*f'^{\times}R\nu_{Y',*}L$ are bounded below
and of étale origin: the étale right adjoints $f^{\times}$, $f'^{\times}$
carry bounded-below objects to bounded-below ones, the étale
compact-support functors having finite cohomological dimension, and
$Rg'_*\nu_{X'}^*\cong\nu_X^*Rg'_{\mathrm{et},*}$ on bounded-below objects
by [prop-weil-pbc-comparison-direct-image], $g'$ being quasi-compact and
quasi-separated. Taking $K$ to be each of these two objects, the Yoneda
argument in the full subcategory of bounded-below objects of étale origin
shows that $\beta^{\vee}_L$ is an isomorphism.
