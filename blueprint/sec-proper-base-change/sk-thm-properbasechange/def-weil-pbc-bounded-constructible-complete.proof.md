+++
kind  = "proof"
of    = "def-weil-pbc-bounded-constructible-complete"
uses = ["sk-prop-integral-criterion", "det-prop-integral-criterion-reductions", "det-lem-int-integral-heart-local-model", "sk-thm-pe-constructible-comparison", "sk-prop-sf-comparison", "sk-def-pe-derived-completion"]
+++
We prove the characterization for $(A,I)=(\mathcal O_E,(\varpi))$, where
$A_T=\mathcal O_{E,T}$. Multiplication by $\varpi$ is injective on
$\mathcal O_{E,T}=\varprojlim_n(A_{E,n})_T$, so the Koszul complex
$[A_T\xrightarrow{\varpi^m}A_T]$ is a resolution of $(A_{E,m})_T$. Hence the intrinsic
completion of [def-weil-pbc-intrinsic-completion] is
$R\varprojlim_m K\otimes^L_{\mathcal O_{E,T}}(A_{E,m})_T$, and derived $I$-completeness is
derived completeness in the sense of [sk-def-pe-derived-completion].

*The tower conditions imply constructibility.* Let $K$ be derived complete with a uniformly
bounded constructible reduction tower. On each stratum $T_\alpha$, pro-étale locally,
$K_1\cong L_{\alpha j}\otimes^L_{A_T}(P_1)_T$ is a bounded complex whose cohomology sheaves
are finite and lisse. So $K_1$ is bounded with constructible cohomology sheaves,
$K_1\in\Dbc(T,A_{E,1})$. By the integral criterion [sk-prop-integral-criterion],
$K\in\Dbc(T,\mathcal O_E)$.

*Constructibility implies the tower conditions.* Let $K\in\Dbc(T,\mathcal O_E)$, with
cohomology in $[a,b]$. It is derived complete by [sk-prop-integral-criterion]. By
[det-lem-int-integral-heart-local-model] (1) there is a finite stratification
$T=\coprod_\alpha T_\alpha$ such that, on a pro-étale cover $\{U_{\alpha j}\to T_\alpha\}$,
$K|_{U_{\alpha j}}\cong M^\bullet\otimes_{\mathcal O_E}\mathcal O_{E,U_{\alpha j}}$ for a
bounded complex $M^\bullet$ of finite free $\mathcal O_E$-modules.

By (2) of the same lemma, $H^q(K|_{U_{\alpha j}})$ is the completion of the finitely
generated module $H^q(M^\bullet)$. Finitely generated $\mathcal O_E$-modules are already
complete, so $H^q(M^\bullet)=0$ for $q\notin[a,b]$. Since $\mathcal O_E$ is a principal
ideal domain, $M^\bullet$ is then quasi-isomorphic to a complex of finite free modules in
degrees $[a-1,b]$, and we take $M^\bullet$ of this form.

Put $L_{\alpha j}=M^\bullet\otimes_{\mathcal O_E}\mathcal O_{E,U_{\alpha j}}$. Its terms
are finite free $A_T|_{U_{\alpha j}}$-modules, it is supported in $[d_0,d_1]=[a-1,b]$, and
its reductions $M^\bullet\otimes_{\mathcal O_E}(A_{E,n})_{U_{\alpha j}}$ have finite lisse
cohomology. The isomorphisms
$K_n|_{U_{\alpha j}}\cong L_{\alpha j}\otimes^L_{A_T}(P_n)_T|_{U_{\alpha j}}$ are obtained
from the one for $K$ by base change, so they intertwine the transition maps. So the tower
is uniformly bounded constructible.

Each $K_n$ lies in $\Dbc(T,A_{E,n})$ by [det-prop-integral-criterion-reductions], so it
comes from the étale site by [sk-thm-pe-constructible-comparison]. The étale witness is
unique up to unique isomorphism, because $\nu_T^*$ is fully faithful on $D^+$
([sk-prop-sf-comparison]). For the same reason the normalization isomorphisms
$K_{n+1}\otimes^L_{P_{n+1}}P_n\cong K_n$ descend uniquely to the witnesses, and they
satisfy the cocycle there. So the étale origins are compatible.
