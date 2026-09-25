+++
id = "lem-trf-trace-source-etale-pullback"
kind = "lemma"
title = "Pullback of the trace-class source"
order = 2501
uses = ["def-trf-etale-base-change", "def-trf-trace-class-source", "def-weil-site-perfect-complex", "lem-trf-etale-exceptional-pullback", "thm-trf-internal-hom-pullback"]
+++
In the situation of [def-trf-etale-base-change], assume
$Lc_2^*K$ site-perfect
and the admissibility of
[lem-trf-etale-exceptional-pullback]. Then there is a canonical
isomorphism

$$
Le_C^*\mathcal H_c(K)\xrightarrow{\ \sim\ }\mathcal H_{c'}(K')
$$

of the trace-class sources.

## Proof

By [def-trf-trace-class-source],
$\mathcal H_c(K)=R\mathcal Hom_A(Lc_2^*K,Rc_1^!K)$. Applying the
internal-Hom/pullback comparison
[thm-trf-internal-hom-pullback] to the site-perfect complex
$Lc_2^*K$ gives a canonical isomorphism

$$
Le_C^*R\mathcal Hom_A(Lc_2^*K,Rc_1^!K)
\xrightarrow{\ \sim\ }
R\mathcal Hom_A\bigl(Le_C^*Lc_2^*K,Le_C^*Rc_1^!K\bigr),
$$

and the base-change identifications
$Le_C^*Lc_2^*K\cong Lc_2'^*K'$ and
$Le_C^*Rc_1^!K\cong Rc_1'^!K'$ of
[def-trf-etale-base-change] and
[lem-trf-etale-exceptional-pullback] transport it to
$R\mathcal Hom_A(Lc_2'^*K',Rc_1'^!K')=\mathcal H_{c'}(K')$.
