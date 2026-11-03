+++
kind = "proof"
of = "det-ctf-finite-comparison-whole"
+++
Let $\mathcal B$ be a basis of the étale site of $X$ consisting of quasi-compact separated étale $u\colon U\to X$
(affine ones suffice). For each $u$, $u_!A_U$ is the free sheaf represented by $U$; it is flat (stalks are
free $A$-modules on the finite geometric fibres of $u$) and constructible ($u$ is quasi-finite and
separated, so $u_!A_U$ is constructible), hence lies in $\Dctf(X_{\mathrm{ét}},A)$.

*Compactness.* By [det-ctf-finite-compact-etale], each $u_!A_U$ is compact in $\D(X_{\mathrm{ét}},A)$.

*Detection.* $\Hom(u_!A_U[n],K)=\Hom(A_U[n],u^*K)=H^{-n}(U,K)$. If these vanish for all $u\in\mathcal B$ and all
$n$, then the cohomology sheaves of $K$ vanish: $\mathcal H^{q}(K)$ is the sheafification of
$U\mapsto H^q(U,K)$, which is zero on the basis $\mathcal B$. So $K=0$.

*Generation.* The set $G=\{u_!A_U[n]\}$ is a set of compact objects of $\D(X_{\mathrm{ét}},A)$ detecting zero
objects. By the compact generation theorem (Neeman; Stacks, Tag 09SN), the localizing subcategory generated
by $G$ is all of $\D(X_{\mathrm{ét}},A)$. Since $G\subset\Dctf(X_{\mathrm{ét}},A)$,
$\D(X_{\mathrm{ét}},A)=\Loc(G)\subset\Loc(\Dctf(X_{\mathrm{ét}},A))\subset\D(X_{\mathrm{ét}},A)$.
