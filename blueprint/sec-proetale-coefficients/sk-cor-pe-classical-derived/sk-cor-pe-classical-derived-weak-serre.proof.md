+++
kind = "proof"
of = "det-pe-classical-derived-weak-serre"
+++
By [det-pe-classical-sheaves-modules], a module sheaf is classical if and only
if it is isomorphic to some $\nu_X^*F$, if and only if its counit
$\nu_X^*\nu_{X,*}G\to G$ is an isomorphism. The zero sheaf is $\nu_X^*0$.

*Kernels and cokernels.* Write $G\cong\nu_X^*F$ and $G'\cong\nu_X^*F'$. By full
faithfulness, $f$ corresponds to $\nu_X^*\varphi$ for a unique
$\varphi\colon F\to F'$. Since $\nu_X^*$ is exact,
$\ker f\cong\nu_X^*\ker\varphi$ and $\operatorname{coker}f\cong
\nu_X^*\operatorname{coker}\varphi$, which are classical.

*Extensions.* Let $0\to G'\to E\to G\to0$ be exact with $G'\cong\nu_X^*F'$ and
$G\cong\nu_X^*F$. Applying the left exact functor $\nu_{X,*}$ gives the exact
sequence

$$
0\to\nu_{X,*}G'\to\nu_{X,*}E\to\nu_{X,*}G\to R^1\nu_{X,*}G'.
$$

By the derived unit isomorphism $F'\xrightarrow{\sim}R\nu_{X,*}\nu_X^*F'$ of
[sk-prop-sf-comparison], $R^1\nu_{X,*}G'\cong H^1(F')=0$, so
$0\to\nu_{X,*}G'\to\nu_{X,*}E\to\nu_{X,*}G\to0$ is exact. Apply the exact
functor $\nu_X^*$. The counits give a map of short exact sequences

$$
\begin{array}{ccccccccc}
0&\to&\nu_X^*\nu_{X,*}G'&\to&\nu_X^*\nu_{X,*}E&\to&\nu_X^*\nu_{X,*}G&\to&0\\
&&\downarrow&&\downarrow&&\downarrow&&\\
0&\to&G'&\to&E&\to&G&\to&0
\end{array}
$$

whose outer vertical maps are isomorphisms because $G'$ and $G$ are classical.
By the five lemma the middle counit is an isomorphism, so $E$ is classical.
