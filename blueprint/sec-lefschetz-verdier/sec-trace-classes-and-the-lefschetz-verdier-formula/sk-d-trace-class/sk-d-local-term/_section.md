+++
id = "sk-d-local-term"
kind = "definition"
title = "Local terms"
order = 3785
uses = ["sk-d-corr", "sk-d-integral", "sk-d-pairing", "sk-d-six", "sk-d-trace-class"]
+++
Let $E$ be proper over $s$, let $\alpha:A_E\to\omega_E$ be a Borel–Moore
section, and let $j_B:B\hookrightarrow E$ be an open immersion with closed
image. The clopen piece $B$ cuts out an idempotent

$$
e_B:A_E\longrightarrow Rj_{B*}j_B^*A_E\simeq j_{B!}j_B^*A_E\longrightarrow A_E,
$$

the unit of $j_B^*\dashv Rj_{B*}$ followed by the counit of $j_{B!}\dashv j_B^*$.
Define the local term of $\alpha$ along $B$ by integration:

$$
\LT_B(\alpha):=\int_E\alpha\circ e_B\in A,
$$

which is $\int_B\alpha|_B$. For an opposite pair $(C,c,u),(D,d,v)$ with
$E=E(C,D)$ proper over $s$, put $\LT_B(u,v):=\LT_B(\langle u,v\rangle_{\mathrm{LV}})$.
For an endocorrespondence with $\Fix(c)$ proper over $s$ and $B\subseteq\Fix(c)$
clopen, use its trace class to set $\LT_B(u):=\LT_B(\Tr_c(u))$; it
equals $\LT_B(u,1_K)$ because $\Tr_c(u)=\langle u,1_K\rangle_{\mathrm{LV}}$
([lem-trf-trace-class-diagonal-pairing]).
At a Frobenius fixed point,
$\LT_{\bar x}$ means the local term on its reduced clopen point component.
