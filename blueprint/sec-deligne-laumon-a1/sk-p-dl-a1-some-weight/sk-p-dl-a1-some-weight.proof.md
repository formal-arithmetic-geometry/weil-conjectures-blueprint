+++
kind  = "proof"
of    = "sk-p-dl-a1-some-weight"
+++
Set $M^c=M^\vee\otimes T_w$, where the Frobenius scalar of $T_w$ maps
to $q^w$ under $\iota$. On a common dense lisse open the paired complex

$$
\DLAFT_\psi(j_!M[1])\oplus
\DLAFT_{\psi^{-1}}(j_!M^c[1])
$$

is $H[1]$ for a lisse sheaf $H$. Zero extension preserves conjugacy
of all point traces, including at the missing points where both
stalks are zero. The Fourier trace identity yields

$$
\iota t_{H,n}(y)=-\sum_{x\in U_0(\mathbf F_{q^n})}
\left(a_x\psi_n(xy)+\overline{a_x}\psi_n(xy)^{-1}\right),
\qquad a_x=\iota t_{M,n}(x).
$$

This is real for every finite extension. At a fixed closed point, all
Frobenius power traces are therefore real; Newton identities imply
that its characteristic polynomial is real. Hence $H$ is $\iota$-real.
The transform $\DLAFT_\psi((j_*M)[1])$ is also the middle extension of
an irreducible lisse sheaf, and two lisse sheaves with isomorphic
shifted middle extensions agree on a common dense open; so, after
shrinking the open, $M'$ is irreducible there. The correction sequence
makes $M'$ on this open an irreducible constituent of $H$, so real-sheaf purity gives a weight $v$.
Semicontinuity applied to $M'$ and its lisse dual extends purity to
its full lisse domain. Forming the envelope after zero extension is
what avoids assuming reality of $j_*M$.
