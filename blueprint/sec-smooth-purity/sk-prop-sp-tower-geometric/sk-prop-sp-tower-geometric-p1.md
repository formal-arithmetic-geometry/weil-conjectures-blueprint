+++
id = "det-sp-tower-p1-adjunction"
kind = "lemma"
title = "The projective-line adjunction for towers"
uses = ["det-sp-tower-classes", "det-sp-tower-shriek-levels"]
+++
Let $q:\mathbf P^1_S\to S$, and let $p_1,p_2:\mathbf P^1_S\times_S\mathbf P^1_S\to\mathbf P^1_S$
be the projections. Define, for $K_\bullet\in D(\operatorname{Tow}(S,\mathcal O_E))$ and
$M_\bullet\in D(\operatorname{Tow}(\mathbf P^1_S,\mathcal O_E))$,

$$
\begin{aligned}
\varepsilon_\bullet(K_\bullet):\ &Rq_{*,\bullet}(q_\bullet^*K_\bullet(1)[2])
\simeq K_\bullet\otimes^{\mathbf L}Rq_{*,\bullet}(\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet)(1)[2]
\xrightarrow{\ \mathrm{id}\otimes\operatorname{Tr}_{q,\bullet}\ }K_\bullet,\\
\eta_\bullet(M_\bullet):\ &M_\bullet\simeq Rp_{2*,\bullet}\Delta_*M_\bullet
\xrightarrow{\ Rp_{2*,\bullet}(\delta_\bullet\otimes p_1^*M_\bullet)\ }
Rp_{2*,\bullet}p_1^*M_\bullet(1)[2]\simeq q_\bullet^*Rq_{*,\bullet}M_\bullet(1)[2],
\end{aligned}
$$

with $\operatorname{Tr}_{q,\bullet}$ and $\delta_\bullet$ from [det-sp-tower-classes].
Then $\eta_\bullet$ and $\varepsilon_\bullet$ are the unit and counit of an
adjunction $Rq_{*,\bullet}\dashv q_\bullet^*(-)(1)[2]$ in $D(\operatorname{Tow})$, whose
evaluation at level $n$ is the finite projective-line adjunction.
