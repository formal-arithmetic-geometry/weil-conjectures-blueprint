+++
kind  = "proof"
of    = "lem-kun-kunneth-via-0f1n"
+++
Denote $a:X\times_kY\to\Spec(k)$, $b:X\to\Spec(k)$ and
$c:Y\to\Spec(k)$. The description of the etale site of a
separably closed point in [lem-kun-03qu-sep-closed] identifies
its sheaves with modules and $Rc_*K$ with $\RGamma(Y_{\Et},K)$.
Put $P=\RGamma(X_{\Et},E)$, $Q=\RGamma(Y_{\Et},K)$, and write
$\varepsilon_b:b^{-1}P\to E$ and
$\varepsilon_c:c^{-1}Q\to K$ for the counits.
By [def-kun-kunneth-map], the adjoint of $\kappa_{E,K}$
under $a^{-1}\dashv Ra_*$ is the tensor product of the pulled-back
counits. We compute the adjoint of the asserted composite.

The projection-formula map of [lem-kun-0f12] is adjoint to

$$
b^{-1}(P\kunotimes{\kunZn}Q)
\cong b^{-1}P\kunotimes{\kunZn}b^{-1}Q
\xrightarrow{\ \varepsilon_b\otimes1\ }
E\kunotimes{\kunZn}b^{-1}Q,
$$

the isomorphism being that of [lem-kun-inverse-image-monoidal].
By its construction from the exchange morphism of
[def-kun-unbounded-exchange], the map $\varphi$ of
[lem-kun-0f1n] is adjoint under
$\pr_1^{-1}\dashv R\pr_{1,*}$ to

$$
\pr_1^{-1}E\kunotimes{\kunZn}a^{-1}Q
\xrightarrow{\ 1\otimes\pr_2^{-1}\varepsilon_c\ }
\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K,
$$

where $a=c\pr_2=b\pr_1$. Composing adjunctions, using the
Leray identification of [lem-kun-leray-unbdd], therefore gives
the adjoint

$$
a^{-1}(P\kunotimes{\kunZn}Q)
\xrightarrow{\ \pr_1^{-1}\varepsilon_b\otimes
\pr_2^{-1}\varepsilon_c\ }
\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K.
$$

This is exactly the defining adjoint of $\kappa_{E,K}$; the
adjunction bijection proves equality of the two maps.
