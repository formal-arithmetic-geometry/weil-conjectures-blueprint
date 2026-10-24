+++
kind  = "proof"
of    = "cor-mg-central-determinant-weight"
+++
*The matrix map is a homomorphism.* For $(h',n),(h'',p)$ in
$G_{\mathrm{arith}}(\rho_Q)$, the product
$(h'\alpha^n(h''),n+p)$ of [def-wf-arithmetic-monodromy-extension] has
matrix
$h'\rho_Q(s)^nh''\rho_Q(s)^{-n}\rho_Q(s)^{n+p}
=(h'\rho_Q(s)^n)(h''\rho_Q(s)^p)$. If $w\in W$ has degree $n$,
then $ws^{-n}\in P$ by [d-monodromy], so $(\rho_Q(ws^{-n}),n)$ lies in
$G_{\mathrm{arith}}(\rho_Q)$ and its matrix is $\rho_Q(w)$.

*The general scalar case.* Let
$\chi_{\det}=\det\circ\rho_Q:W\to k^\times$ be the character of
the determinant line of $Q$, and put $c=\chi_{\det}(s)$. Write
$\Phi_Q(z)=(h_Q,m)$ with $h_Q\in H(\rho_Q)$; the degree
is $m$ because $\Phi_Q$ preserves degrees
([lem-mg-degree-component-functoriality]). By hypothesis its matrix is
$h_Q\rho_Q(s)^m=c_Q1_Q$, and taking determinants on the $r$-dimensional
space $Q$ gives

$$
c_Q^r=\det(h_Q)\,c^m .
$$

The morphism $\Delta_{\rho_Q}$ of
[lem-mg-determinant-monodromy-morphism] sends $\Phi_Q(z)$ to
$(\det h_Q,m)$ in the arithmetic monodromy group of the rank-one
determinant line. The group $A=\chi_{\det}(P)$ is finite by
hypothesis, hence Zariski closed in $\mathbf G_m$. The determinant is a
regular function on $\operatorname{GL}(Q)$, so the inverse image of $A$
under it is a closed subset of $\operatorname{GL}(Q)$; it contains
$\rho_Q(P)$, hence its Zariski closure
$H(\rho_Q)$. Therefore $a:=\det h_Q\in A$; in the
notation of [def-wf-degree-components], $(a,m)$ is the degree-$m$
element $\Delta_{\rho_Q}(\Phi_Q(z))$. The element $a$ has finite order, and a real weight
character kills finite-order elements: if $a^e=1$ with $e>0$, then
$e\lambda(a)=\lambda(a^e)=0$. Applying $\lambda$ therefore gives
$r\lambda(c_Q)=m\lambda(c)$, that is,

$$
\frac{\lambda(c_Q)}{m}=\frac{\lambda(c)}{r}=\dw_\lambda(Q)
$$

by the definition in [d-weights]. Only the scalar action of $z$ on $Q$
was used here, not the irreducibility or semisimplicity of $Q$.

*Irreducible $Q$.* By [lem-mg-degree-component-functoriality],
$\Phi_Q(z)$ is central in $G_{\mathrm{arith}}(\rho_Q)$. By the first
paragraph its matrix commutes with the matrix $\rho_Q(w)$ of every
$(\rho_Q(ws^{-n}),n)$, i.e. with the whole image of $W$. If $Q$ is
irreducible, [lem-wf-schur-scalar] makes this matrix a scalar
$c_Q$, nonzero because the matrix is invertible. Taking $V=Q$ and
$\Phi_Q$ the identity gives the stated case of $\rho_{\mathcal W}$, and the
case $\lambda=\lambda_\iota$ is the last display.

*Independence of the lift.* Replacing the degree-one element by $us$
with $u\in P$ multiplies $\chi_{\det}(s)$ by the finite-order
element $\chi_{\det}(u)\in A$, which $\lambda$ kills; so
$\dw_\lambda(Q)$ does not depend on the degree-one lift.
