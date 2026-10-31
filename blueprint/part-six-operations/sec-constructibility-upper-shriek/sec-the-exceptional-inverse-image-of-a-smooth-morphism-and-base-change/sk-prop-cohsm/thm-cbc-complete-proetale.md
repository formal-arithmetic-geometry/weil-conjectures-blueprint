+++
id = "thm-cbc-complete-proetale"
kind = "theorem"
title = "Integral compact-support base change"
order = 2632
uses = ["det-def-sfb-dc-setting", "det-def-sfb-condensed-ring", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-dc-lower-shriek", "det-def-sfb-shriek-base-change-morphism", "def-pe-derived-complete", "sk-prop-integral-criterion"]
+++
Work in the setting of [det-def-sfb-dc-setting]. Let $E/\Ql$ be a finite
extension with ring of integers $\mathcal O_E$ and uniformizer $\pi_E$, regard
$\mathcal O_E$ as the condensed ring $\underline{\mathcal O}_E$
([det-def-sfb-condensed-ring]), and put $\mathcal O_{E,X}=p_X^*\mathcal O_E$
([det-def-sfb-pulled-back-coefficients]). Let

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

be a cartesian square of the setting, let $c$ be a compactification of $f$ and
$c'$ its base change. Then the compact-support base change morphism of
[det-def-sfb-shriek-base-change-morphism]

$$
\Ex^c_!(K):Lg^*Rf^c_!K\xrightarrow{\ \sim\ }Rf'^{\,c'}_!Lg'^*K
$$

is an isomorphism for every $K\in\Dbc(X,\mathcal O_E)$, natural in $K$; here
$Rf^c_!=Rp_*\circ i_!$ is the lower shriek of [det-def-sfb-dc-lower-shriek]
on the condensed categories $\Dbc(-,\mathcal O_E)$. For proper $f$ and
$c=(\mathrm{id},f)$ it is the proper base change isomorphism
$Lg^*Rf_*K\cong Rf'_*Lg'^*K$.

No completed pullback enters: $Lg^*$ and $Lg'^*$ preserve
$\Dbc(-,\mathcal O_E)$, whose objects are derived $\pi_E$-complete
$\mathcal O_{E,X}$-complexes ([def-pe-derived-complete],
[sk-prop-integral-criterion]), so the ordinary pullback of a constructible
integral complex is already complete.
