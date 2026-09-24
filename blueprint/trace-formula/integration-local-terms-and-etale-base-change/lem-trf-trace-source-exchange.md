+++
id = "lem-trf-trace-source-exchange"
kind = "lemma"
title = "Exchange of the trace-class sources"
order = 3905
uses = ["def-trf-admissibility", "def-trf-coefficient-pushforward", "def-trf-trace-class-source"]
+++
In the setting of [def-trf-coefficient-pushforward], the diagram of
supported sections

$$
\begin{gathered}
A_D\xrightarrow{\ \widetilde{[f,g]_!u}\ }
\mathcal H_b(K')\\
\uparrow\hphantom{\sim}\\
Rg_*A_C\xrightarrow{\ Rg_*\widetilde u\ }Rg_*\mathcal H_c(K)
\end{gathered}
$$

commutes, where the left vertical arrow is the unit
$A_D\to Rg_*A_C$, $\widetilde u$ and
$\widetilde{[f,g]_!u}$ are the mates of $u$ and $[f,g]_!u$ of
[def-trf-trace-class-source], and the right vertical arrow is the
exchange isomorphism

$$
Rg_*\mathcal H_c(K)
=Rg_*R\mathcal Hom_A(c_2^*K,c_1^!K)
\xrightarrow{\ \sim\ }
R\mathcal Hom_A(b_2^*K',b_1^!K')
=\mathcal H_b(K')
$$

of [def-trf-admissibility].

## Proof

By [def-trf-trace-class-source], the mate $\widetilde u$ is the
image of $u$ under the tensor–internal-Hom adjunction

$$
\Hom_{D(C,A)}(A_C,R\mathcal Hom_A(c_2^*K,c_1^!K))
\cong
\Hom_{D(C,A)}(c_2^*K,c_1^!K).
$$

The exchange isomorphism on the right is, by
[def-trf-admissibility], the exceptional-adjoint of the ordinary
exchange; the commutativity of the diagram is therefore the naturality
of this adjunction in the two legs, which is precisely the coherence
datum relating the exchange to the adjunction units and counits recorded
in [def-trf-admissibility]. Hence the diagram commutes.
