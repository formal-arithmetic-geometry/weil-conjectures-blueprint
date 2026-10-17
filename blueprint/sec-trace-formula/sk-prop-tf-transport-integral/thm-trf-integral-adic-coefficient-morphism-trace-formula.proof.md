+++
kind  = "proof"
of    = "thm-trf-integral-adic-coefficient-morphism-trace-formula"
+++
*(1).* By [prop-trf-adic-coefficient-morphism-systems], items (1) and (3),
each $P_n$ and $P_{\bar y,n}$ is perfect and the families
$(F_{c,m}(\psi_n))_n$ and $(\psi_{n,m,\bar y})_n$ are compatible; by its
item (2) they have lifts, and by its item (4) the traces of any lifts are
the compatible systems
$$
\operatorname{tr}_{\mathcal O_E}(V_m)=\bigl(\operatorname{tr}_{A_n}(F_{c,m}(\psi_n)\mid P_n)\bigr)_n,
\qquad
\operatorname{tr}_{\mathcal O_E}(V_{y,m})=\bigl(\operatorname{tr}_{A_n}(\psi_{n,m,\bar y}\mid P_{\bar y,n})\bigr)_n .
$$
At each level $n$, [thm-trf-coefficient-morphism-trace-formula], applied to
$(K_n,\psi_n)$ under the assumed hypotheses (it requires no invertibility of
$\psi_n$), gives
$$
\operatorname{tr}_{A_n}\bigl(F_{c,m}(\psi_n)\mid P_n\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}\operatorname{tr}_{A_n}\bigl(\psi_{n,m,\bar y}\mid P_{\bar y,n}\bigr)
\quad\text{in }A_n,
$$
with the stalk endomorphism normalized as there and in
[prop-trf-adic-coefficient-morphism-systems]. The index set
$X_0(\mathbf F_{q^m})$ is finite ($X_0$ is of finite type over $k_0$) and the
same for all $n$, and the reduction $\mathcal O_E\to A_n$ is additive. Hence
$\operatorname{tr}_{\mathcal O_E}(V_m)$ and $\sum_y\operatorname{tr}_{\mathcal O_E}(V_{y,m})$
have the same image in every $A_n$, and they are equal because
$\mathcal O_E\to\varprojlim_nA_n$ is injective.

*(2).* By [prop-trf-rational-frobenius-integral-model], item (2), the
$\psi_n$ form a compatible system of Frobenius coefficient morphisms on the
reduction tower of $K_{\mathcal O}$; this tower, with the associativity
isomorphisms $K_{n+1}\otimes^L_{A_{n+1}}A_n\cong
K_{\mathcal O}\otimes^L_{\mathcal O_E}A_n=K_n$ as $\nu_n$, is a normalized
$A_\bullet$-system of [def-trf-adic-system], its levels lying in
$D^b_{ctf}(X,A_n)$ by hypothesis. For it
$P_{\mathcal O}=R\Gamma_c(X,K_{\mathcal O})$ and
$P_{\bar y,\mathcal O}=K_{\mathcal O,\bar y}$
([prop-trf-adic-coefficient-morphism-systems]). By items (3) and (4) of
[prop-trf-rational-frobenius-integral-model], $U_m$ is the derived limit of
the levelwise operators $F_{c,m}(\psi_n)$ and $U_{y,m}$ that of the
$\psi_{n,m,\bar y}$, i.e. $\mathrm{pr}_n\circ U_m=F_{c,m}(\psi_n)\circ\mathrm{pr}_n$
and likewise for the stalks; so by item (2) of
[prop-trf-adic-coefficient-morphism-systems] they are lifts of the two
compatible families, and (1) gives the identity.
