+++
kind = "proof"
of = "dag-det-pe-hypercover-existence"
tags = ["sheaf-dag"]
uses = ["dag-det-pe-hypercover-product-wcontractible", "dag-det-pe-hypercover-single-cover", "dag-det-pe-hypercover-single-affine", "dag-det-pe-weak-contractible-equivalences"]
+++
1. Apply the product theorem and singleton-cover theorem. Obtain the affine simplicial object and covering matching cones from the geometric realization theorem. For each degree, rewrite its object using the supplied spectrum equality and apply the final affine clause of det-pe-weak-contractible-equivalences. Assemble the three conclusions by conjunction introduction. (uses [dag-det-pe-hypercover-product-wcontractible], [dag-det-pe-hypercover-single-cover], [dag-det-pe-hypercover-single-affine], [dag-det-pe-weak-contractible-equivalences])
