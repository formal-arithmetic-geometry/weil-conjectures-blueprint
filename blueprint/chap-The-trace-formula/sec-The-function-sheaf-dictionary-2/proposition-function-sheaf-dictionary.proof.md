+++
kind = "proof"
of = "proposition-function-sheaf-dictionary"
order = 1029
uses = ["definition-trace-function"]
+++
Part (5) is Theorem [theorem-grothendieck-lefschetz-trace-formula] and part (3)
is Corollary [corollary-trace-functions-direct-image-compact].

For (1), the stalk of $g^*K$ at $\bar w$ is $K_{\bar x}$ with $x=g_0(w)$, and
the Weil structure of $g^*K$ is $g^*\phi$ composed with the base change
isomorphism. Under this identification of stalks the $m$-th iterate of the
Weil structure of $g^*K$ at $\bar w$ is the $m$-th iterate of $\phi$ at
$\bar x$, so the two Frobenius endomorphisms agree.

For (2), the stalk of $K\otimes^{\mathbf L}_\Lambda L$ at $\bar x$ is
$K_{\bar x}\otimes^{\mathbf L}_\Lambda L_{\bar x}$, since pullback to
$\bar x$ commutes with derived tensor products, and its Frobenius is the
tensor product of the two Frobenius endomorphisms. These stalks are perfect (Lemma [lemma-perfect-complexes-geometric-point]), so we may represent them by
bounded complexes $P$, $Q$ of finite projective modules and the endomorphisms by
chain maps $v$, $w$. Now the term of degree $n$ of $P\otimes Q$ is
$\bigoplus_{i+j=n}P^i\otimes Q^j$, the trace of $v^i\otimes w^j$ on
$P^i\otimes Q^j$ is $\operatorname{Tr}(v^i)\operatorname{Tr}(w^j)$, and
$(-1)^n=(-1)^i(-1)^j$. By the chain formula of
Proposition [proposition-properties-trace] the trace on $P\otimes Q$ is
therefore the product of the traces on $P$ and on $Q$.

For (4), note that $j_!=Rj_!$ and $i_*=Ri_!$, with the same Weil structures.
By (3), $t_{j_!j^*K,m}(x)$ is the sum of $t_{j^*K,m}$ over the fibre of $j_0$
at $x$. This fibre is the point $x$ if $x\in U_0$, and it is empty otherwise.
By (1), $t_{j^*K,m}(x)=t_{K,m}(x)$ for $x\in U_0(\mathbf F_{q^m})$. The same
argument applies to $i_*i^*K$, and the two functions add up to $t_{K,m}$.
