+++
id = "det-def-sfb-shriek-base-change-morphism-definition"
kind = "definition"
title = "The compact-support base change morphism $\\mathrm{Ex}_!^c$"
uses = ["det-def-sfb-shriek-base-change-morphism-compactification", "det-def-sfb-base-change-morphism-bc", "def-sfb-dc-open-base-change-inverse", "thm-sfb-dc-open-base-change-iso", "det-def-sfb-dc-lower-shriek-definition"]
+++
In the situation of [det-def-sfb-shriek-base-change-morphism-compactification], let $\Lambda$ be a
commutative condensed ring as in [det-def-sfb-dc-lower-shriek-definition] (derived pushforwards
restrict to $D_{\mathrm{cons}}$), so that $Rf_!^c=Rp_*\circ i_!$ and $Rf'^{\,c'}_!=Rp'_*\circ i'_!$ are
defined. Let

- $\mathrm{BC}\colon Lg^*Rp_*\Rightarrow Rp'_*L\bar g^*$ be the base change morphism of
  [det-def-sfb-base-change-morphism-bc] for the right (proper) square, with $f,f',g,g'$ there
  replaced by $p,p',g,\bar g$;
- $\mathrm{Ex}^j\colon i'_!Lg'^*\xrightarrow{\sim}L\bar g^*i_!$ be the extension-by-zero exchange
  isomorphism of the left (cartesian, open) square, invertible by [thm-sfb-dc-open-base-change-iso],
  with inverse the base change isomorphism $L\bar g^*i_!\xrightarrow{\sim}i'_!Lg'^*$ of
  [def-sfb-dc-open-base-change-inverse].

The *compact-support base change morphism* is the natural transformation of functors
$D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(Y',\Lambda)$
$$
\mathrm{Ex}_!^c\colon Lg^*\circ Rf_!^c=Lg^*Rp_*i_!\xrightarrow{\ \mathrm{BC}_{i_!}\ }Rp'_*L\bar g^*i_!\xrightarrow{\ Rp'_*(\mathrm{Ex}^j)^{-1}\ }Rp'_*i'_!Lg'^*=Rf'^{\,c'}_!\circ Lg'^* .
$$
It depends on the compactification $c$; independence of $c$ is not asserted. The second arrow is a
natural isomorphism.
