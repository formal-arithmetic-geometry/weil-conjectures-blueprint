+++
kind = "proof"
of = "det-base-field-cd-galois-group"
+++
A finite extension $L/K$ of degree $n$ has $q^n$ elements, and its multiplicative
group has order $q^n-1$, so every element of $L$ is a root of $T^{q^n}-T$. This
polynomial is separable (its derivative is $-1$) and has at most $q^n$ roots, so
$L$ is exactly its set of roots in $K^{\rm sep}$. Hence the degree-$n$
subextension is unique, and it is the splitting field of a separable polynomial,
hence Galois of order $n$. The Frobenius $\phi$ fixes $K$ and is an automorphism
of $L$. If $\phi$ had order $d<n$ on $L$, all $q^n$ elements of $L$ would be roots
of $T^{q^d}-T$, which has at most $q^d<q^n$ roots; so $\phi$ has order $n$ and
generates the cyclic group $\operatorname{Gal}(L/K)\cong\mathbf Z/n$, with $\phi$
corresponding to $1$.

The finite subextensions $K_n$ are directed by divisibility, $K_d\subseteq K_n$
for $d\mid n$, and the restriction maps send $\phi$ to $\phi$, i.e. they are the
reductions $\mathbf Z/n\to\mathbf Z/d$. Since $K^{\rm sep}=\bigcup_nK_n$, Galois
theory gives
$\operatorname{Gal}(K^{\rm sep}/K)=\varprojlim_n\operatorname{Gal}(K_n/K)
\cong\varprojlim_n\mathbf Z/n=\widehat{\mathbf Z}$ as profinite groups.
