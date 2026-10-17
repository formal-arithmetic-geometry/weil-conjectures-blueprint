+++
kind = "proof"
of = "sk-cor-tf-contracting-input"
uses = ["sk-thm-tf-contracting-local-term", "sk-d-trace-class"]
+++
Apply Theorem [sk-thm-tf-contracting-local-term] with $Z=\{y\}$.
Then $C_Z$ is the reduced point $z$ and $\beta_Z=\beta$, so $c_Z$ is
the identity correspondence of the point, with coefficient
$K_{\bar y}$. By the normalization in Definition [sk-d-trace-class],
its local term is the categorical trace. When the first leg is the
identity, the base-change mate in the construction of $u_Z$ is the
identity, so the restricted morphism is the stalk map $u_{\bar y}$.
