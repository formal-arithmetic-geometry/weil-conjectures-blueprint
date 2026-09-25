+++
id = "def-trf-etale-base-change"
kind = "definition"
title = "Etale base change of a correspondence"
order = 2499
uses = ["def-trf-correspondence", "def-weil-scheme-morphism-properties"]
+++
In the setting of [def-trf-correspondence], let $e:X'\to X$ be
etale, let $C'=C\times_{X\times_sX}(X'\times_sX')$ be the base change
of $C$ along $e\times_se$, with induced legs $c_i':C'\to X'$
(so that $c_i'e_C=ec_i$, where $e_C:C'\to C$ is the projection),
and put $K'=Le^*K$. The *base-changed correspondence* of
$u:Lc_2^*K\to Rc_1^!K$ is the composite

$$
e^*u:\quad Lc_2'^*K'\xrightarrow{\ \sim\ }Le_C^*Lc_2^*K
\xrightarrow{\ Le_C^*u\ }Le_C^*Rc_1^!K\xrightarrow{\ \sim\ }Rc_1'^!K',
$$

the first and last arrows being the canonical comparisons for the
cartesian square. The *base-changed fixed scheme* is
$F'=F\times_XX'=\operatorname{Fix}(c')$ with projections
$e_F:F'\to F$ and $d':F'\to X'$, and the square relating $F'$
and $F$ is cartesian.
