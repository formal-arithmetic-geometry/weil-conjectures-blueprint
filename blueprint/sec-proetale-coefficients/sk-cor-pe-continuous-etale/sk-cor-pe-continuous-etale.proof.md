+++
kind = "proof"
of = "sk-cor-pe-continuous-etale"
uses = ["sk-prop-sf-comparison", "sk-prop-pe-continuous-cohomology"]
+++
By [sk-prop-sf-comparison], each
$R\Gamma(X_{\Proet},F_n)$ is identified with $R\Gamma(X_{\Et},F_{n,\Et})$. On the
category of inverse systems, the derived functor of sections followed
by inverse limit is $R\varprojlim_nR\Gamma(X_{\Et},F_{n,\Et})$. To see
this, one may compute with an injective resolution in the diagram category,
or use the derived adjunctions to the constant diagram functor; see
Bhatt–Scholze, *The pro-étale topology for schemes*, Proposition 5.6.2.
