+++
kind  = "proof"
of    = "sk-i-real-compactification"
+++
By [sk-thm-nagata-compactification], $U_0$ is an open subscheme of a
proper $k_0$-scheme. We take the reduced closure of $U_0$ in it and
normalize this closure in $k_0(U_0)$. Since a scheme of finite type
over a field is Nagata, the normalization is finite
([Stacks `035B`](https://stacks.math.columbia.edu/tag/035B),
[Stacks `035S`](https://stacks.math.columbia.edu/tag/035S)), as in the
normalization arguments of [sk-lem-curve-normalization], and it is an
isomorphism over the normal open $U_0$. The resulting proper normal curve is
regular, because a one-dimensional noetherian normal local domain is a
discrete valuation ring, and hence it is smooth over the perfect field $k_0$
([Stacks `0B8Y`](https://stacks.math.columbia.edu/tag/0B8Y)). Its boundary is
zero-dimensional and proper over $k_0$, hence finite, and its reduced
structure is étale because $k_0$ is perfect. After base change to $k$, the
curve $U$ is dense and connected, so its closure $C$ is connected. Finally, a
smooth proper curve is projective: by Riemann–Roch ([sk-thm-picard-rr]), a
sufficiently high multiple of an effective divisor of positive degree has
enough sections to separate points and tangent vectors. Thus $C_0$ is
projective, as the construction of the Jacobian requires
([lem-wf-finite-field-curve-quasi-projective],
[lem-wf-curve-normal-smooth-compactification]).
