+++
kind = "proof"
of = "det-tf-fixed-point-algebra"
uses = ["det-tf-fixed-point-equations"]
+++
The polynomial $t^{q^m}-t=\prod_{\lambda\in\mathbf F_{q^m}}(t-\lambda)$ is separable, with
distinct roots in $k$. By the Chinese remainder theorem
$k[t]/(t^{q^m}-t)\simeq\prod_{\lambda\in\mathbf F_{q^m}}k$, the projection to the
$\lambda$-factor being evaluation at $\lambda$. Tensoring the $r$ one-variable
isomorphisms over $k$ gives the first isomorphism, with the $\lambda$-factor projection
$f\mapsto f(\lambda)$.

Under this isomorphism the image of $\mathfrak a\,k[t]$ is the product of the ideals
$\bigl(f(\lambda):f\in\mathfrak a\bigr)\subset k$. Such an ideal is $0$ if $f(\lambda)=0$ for
all $f\in\mathfrak a$, that is, if $\lambda\in X_0(\mathbf F_{q^m})$, and is $k$ otherwise.
So the quotient keeps exactly the factors at the rational solutions, which gives the
second isomorphism. The factors correspond to idempotents determined by the evaluation
maps, so the identification is canonical and compatible with passing to an open
$U_0\subset X_0$, whose factors are those indexed by $U_0(\mathbf F_{q^m})$. Combined with
[det-tf-fixed-point-equations] this describes the fixed scheme.
