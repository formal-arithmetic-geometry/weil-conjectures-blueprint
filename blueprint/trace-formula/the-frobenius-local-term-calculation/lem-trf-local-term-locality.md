+++
id = "lem-trf-local-term-locality"
kind = "lemma"
title = "Locality of the trace class at a fixed point"
order = 3911
uses = ["def-trf-local-term", "def-trf-trace-class-source", "lem-trf-trace-map-from-external-duality"]
+++
Let $c$ be an admissible correspondence with
$\operatorname{Fix}(c)=F$, and let $y\in F(k)$ be a geometric fixed
point which is an open-and-closed component of $F$. The restriction
$\operatorname{Tr}_c(u)|_y$, and hence the local term
$\operatorname{LT}_y(u)$ of [def-trf-local-term], depend only on
the stalk $K_{\bar y}$ and on the stalk map
$u_{\bar y}:K_{\bar y}\to K_{\bar y}$ induced by $u$, together with
the fixed-point datum $c_1(y)=c_2(y)$.

## Proof

By [def-trf-trace-class-source], the trace-class source is the
internal Hom $\mathcal H_c(K)=R\mathcal Hom_A(c_2^*K,c_1^!K)$, whose
stalk at the fixed point $y$ — using the purity clause of the
six-operations package in relative dimension zero, which identifies
$c_1^!K$ and $c_2^*K$ with $K$ on the fixed scheme — is

$$
\mathcal H_c(K)_{\bar y}\cong R\mathcal Hom_A(K_{\bar y},K_{\bar y}),
$$

and the mate $\widetilde u$ restricts to the mate of $u_{\bar y}$.
By [lem-trf-trace-map-from-external-duality], the trace map is the
composite of the evaluation map $e_K$, the fixed-square base change
and the dualizing composition, all of which are local on the fixed
scheme: their restriction to the open-and-closed component $y$ is
computed from the stalk data alone. Hence the restriction
$\operatorname{Tr}_c(u)|_y$, and the integral of
[def-trf-local-term] over the component $y$, depend only on
$(K_{\bar y},u_{\bar y})$.
