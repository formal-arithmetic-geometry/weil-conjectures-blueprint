+++
kind = "proof"
of = "sk-prop-pe-continuous-cohomology"
uses = ["det-pe-continuous-cohomology-limit", "det-pe-continuous-cohomology-etale", "det-pe-continuous-cohomology-milnor"]
+++
By repleteness ([sk-prop-pe-replete]) $F\simeq R\varprojlim_nF_n$, and derived
global sections, being a right adjoint, commute with derived inverse limits
([det-pe-continuous-cohomology-limit]). The bounded-below cohomology comparison
([sk-prop-sf-comparison]) identifies each $R\Gamma(X_{\Proet},F_n)$ with
$R\Gamma(X_{\Et},F_{n,\Et})$. On the category of inverse systems, the derived
functor of sections followed by inverse limit is
$R\varprojlim_nR\Gamma(X_{\Et},F_{n,\Et})$; one may compute it with an injective
resolution in the diagram category, or use the derived adjunctions to the
constant-diagram functor ([det-pe-continuous-cohomology-etale]). This is
Bhatt–Scholze, Proposition 5.6.2. The exact sequence is the Milnor sequence of
the derived limit ([det-pe-continuous-cohomology-milnor]).
