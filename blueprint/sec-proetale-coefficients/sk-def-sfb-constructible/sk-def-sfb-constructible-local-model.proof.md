+++
kind  = "proof"
of    = "det-def-sfb-constructible-local-model"
+++
$(1)\Rightarrow(2)$. Choose a presentation $\Lambda(*)^m\xrightarrow{A}\Lambda(*)^n\to P_i\to0$.
Passing to constant sheaves is exact, and $\Lambda_{U_i}\otimes_{\Lambda(*)_{U_i}}-$ is right
exact and sends $\Lambda(*)_{U_i}^k$ to $\Lambda_{U_i}^k$. So
$\Lambda_{U_i}^m\xrightarrow{A}\Lambda_{U_i}^n\to\Lambda_{U_i}\otimes_{\Lambda(*)}P_i\to0$ is
exact, with the same matrix $A$.

$(2)\Rightarrow(1)$. Let $P_i=\operatorname{coker}(A\colon\Lambda(*)^m\to\Lambda(*)^n)$, a
finitely presented $\Lambda(*)$-module. By the computation just made,
$\Lambda_{U_i}\otimes_{\Lambda(*)}P_i=\operatorname{coker}(A\colon\Lambda_{U_i}^m\to\Lambda_{U_i}^n)\cong M|_{U_i}$.

Finally (2) is in particular a presentation of $M|_{U_i}$ as the cokernel of a map of finite
free $\Lambda_{U_i}$-modules, which is the definition of local finite presentation
([def-sfb-finitely-presented-module], [def-sfb-locally-finitely-presented]).
