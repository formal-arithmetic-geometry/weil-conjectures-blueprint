+++
id = "det-thm-rationality"
kind = "theorem"
title = "Rationality of the zeta series"
lean = ["AlgebraicGeometry.Scheme.zetaSeries_rational"]
order = 4118
uses = ["det-def-zeta", "det-prop-euler", "sk-cor-tf-point-counting", "prop-weil-integral-rational-series"]
+++
Let $X_0$ be a scheme of finite type (quasi-compact and locally of finite
type) over $\Fq$. Then there are $A,B\in\Z[T]$ with $B(0)=1$ and

$$
B(T)\,Z(X_0,T)=A(T)\quad\text{in }\Q[[T]];
$$

in particular $Z(X_0,T)\in\Q(T)\cap(1+T\Z[[T]])$.
