+++
kind = "proof"
of = "theorem-trace-formula-euler-product--4"
order = 1036010
uses = ["theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "lemma-logarithm-determinant", "theorem-trace-formula-euler-product--1"]
+++
Put $P_s(T)=\prod_{x\in s}\Delta_x(T)^{-1}$. The logarithmic derivative
form of Lemma [lemma-logarithm-determinant], applied to each cohomology
sheaf, gives

$$
T P_s'(T)=A_s(T)P_s(T),\qquad
T C_K'(T)=B(T)C_K(T),
$$

where both $A_s$ and $B$ have constant coefficient zero. For $m\geq1$,

$$
[T^m]A_s(T)=\sum_{\substack{x\in s\\\deg(x)\mid m}}
\deg(x)\sum_{j\in J}(-1)^j
\operatorname{Tr}\bigl(\operatorname{Frob}_x^{m/\deg(x)}
\mid\mathcal H^j(K)_{\bar x}\bigr),
$$

and

$$
[T^m]B(T)=\sum_{i\in S}(-1)^i
\operatorname{Tr}\bigl(\operatorname{Frob}_{X,K}^m
\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr).
$$

Lean obtains these equations from
`LinearMap.X_mul_derivative_inv_alternatingCharpolyRevProd` and the
product rule `PowerSeries.X_mul_derivative_prod`.

For $1\leq m\leq n$, Theorem
[theorem-grothendieck-lefschetz-trace-formula] identifies the second sum
with the sum of the trace function over $X_0(\mathbf F_{q^m})$.
`AlgebraicGeometry.WeilComplex.traceFunction_eq_sum` restricts the
stalk degrees to $J$. At a point over $x$,
`AlgebraicGeometry.WeilSheaf.traceFunction_eq_trace_frobeniusEnd_stalk_pow`
identifies the trace with that of $\operatorname{Frob}_x^{m/\deg(x)}$.
The weighted point-counting formula
`AlgebraicGeometry.Scheme.Hom.finsum_fieldPoints_eq_sum` then groups
these terms by $x$, with multiplicity $\deg(x)$. Every contributing
point belongs to $s$, since $\deg(x)\mid m$ implies $\deg(x)\leq m\leq n$.
Thus $A_s$ and $B$ agree through degree $n$.

Finally, $P_s(0)=C_K(0)=1$, by
`LinearMap.constantCoeff_alternatingCharpolyRevProd`.
`PowerSeries.coeff_eq_of_X_mul_derivative_eq` determines the
coefficients recursively from the differential equations and the
common constant coefficient. It gives the desired equality in degree
$n$. This uses characteristic zero and does not require choosing a
topology on $\overline{\mathbf Q}_\ell[[T]]$.
