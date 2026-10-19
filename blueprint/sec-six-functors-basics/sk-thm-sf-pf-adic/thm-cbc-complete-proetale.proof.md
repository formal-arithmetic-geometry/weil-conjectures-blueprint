+++
kind  = "proof"
of    = "thm-cbc-complete-proetale"
uses = ["sk-def-sfb-dc-restricted-functors", "sk-thm-sfb-proper-base-change", "sk-thm-existence", "sk-def-sfb-open-base-change"]
+++
Write $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$, $c'=(X'\xrightarrow{i'}Z'\xrightarrow{p'}Y')$ and
$\bar g:Z'\to Z$ for the projection. By
[sk-def-sfb-shriek-base-change-morphism], $\Ex^c_!(K)$ is the composite

$$
Lg^*Rp_*i_!K\xrightarrow{\ \mathrm{BC}\ }Rp'_*L\bar g^*i_!K
\xrightarrow{\ (\Ex^{j})^{-1}\ }Rp'_*i'_!Lg'^*K .
$$

The object $i_!K$ lies in $\Dbc(Z,\mathcal O_E)$
([sk-def-sfb-dc-restricted-functors]). The first arrow is the proper base
change map for the cartesian square formed by $p$ and $g$, evaluated on
$i_!K$; it is an isomorphism by [sk-thm-sfb-proper-base-change] with
$\Lambda=\mathcal O_E$, since $\Dctf=\Dbc$ at this coefficient ring
([sk-thm-existence]). The second arrow is $Rp'_*$ applied to the inverse of
the extension-by-zero base change isomorphism of
[sk-def-sfb-open-base-change] for the cartesian open square formed by $i$ and
$\bar g$. Hence $\Ex^c_!(K)$ is an isomorphism. Both arrows are natural
transformations, so the composite is natural in $K$. For proper $f$ and
$c=(\mathrm{id},f)$ the second arrow is the identity and $\Ex^c_!$ is the
proper base change map.
