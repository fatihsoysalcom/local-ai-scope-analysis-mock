def analyze_brief_local_ai_mock(brief_text: str) -> dict:
    """
    Simulates a 'local AI' scope analysis for a project brief.
    It identifies key requirements, potential ambiguities, missing information,
    and potential risks using keyword matching and simple heuristics.
    This demonstrates the concept of ScopeNote's analysis without requiring
    an actual large language model setup.
    """
    brief_text_lower = brief_text.lower()

    # --- 1. Identified Requirements (Keywords) ---
    # These keywords indicate specific features or functionalities requested by the client.
    requirements_keywords = {
        "web sitesi": "Website development",
        "mobil uygulama": "Mobile application",
        "e-ticaret": "E-commerce functionality",
        "ödeme sistemi": "Payment system integration",
        "yönetim paneli": "Admin panel",
        "veritabanı": "Database",
        "api entegrasyonu": "API integration",
        "ürün listeleme": "Product listing",
        "kullanıcı kaydı": "User registration",
        "raporlama": "Reporting features"
    }
    identified_requirements = []
    for keyword, desc in requirements_keywords.items():
        if keyword in brief_text_lower:
            identified_requirements.append(desc)

    # --- 2. Potential Ambiguities / Vague Terms ---
    # These terms are subjective and require further clarification from the client.
    ambiguity_keywords = {
        "modern": "What specific design trends or technologies define 'modern'?",
        "hızlı": "What are the performance benchmarks or load times expected?",
        "kullanıcı dostu": "What specific UX principles or user testing methods are expected?",
        "güzel tasarım": "What are the aesthetic preferences or brand guidelines?",
        "esnek": "Flexible in what aspects (scalability, features, future changes)?",
        "basit": "Simple in terms of UI, features, or underlying complexity?",
        "kolay": "Easy for whom (end-users, admins, developers)?"
    }
    potential_ambiguities = []
    for keyword, question in ambiguity_keywords.items():
        if keyword in brief_text_lower:
            potential_ambiguities.append(f"'{keyword}': {question}")

    # --- 3. Missing Information / Questions to Ask ---
    # These are crucial details often omitted in initial briefs, leading to scope creep.
    missing_info_check = {
        "bütçe": "What is the allocated budget for this project?",
        "zaman çizelgesi": "What is the desired timeline or specific deadline?",
        "hedef kitle": "Who is the primary target audience for this project?",
        "teknoloji yığını": "Are there any preferred technologies or platforms?",
        "bakım": "What are the expectations for post-launch maintenance and support?",
        "referans": "Are there any reference websites or applications?",
        "içerik": "Who will be responsible for providing content (text, images, videos)?"
    }
    questions_to_ask = []
    for keyword, question in missing_info_check.items():
        if keyword not in brief_text_lower:
            questions_to_ask.append(question)

    # --- 4. Potential Risks ---
    # Identifying phrases that might indicate future problems or scope creep.
    risk_indicators = {
        "sınırsız revizyon": "Risk of scope creep and endless iterations.",
        "çok kısa süre": "Risk of rushed work, quality issues, and burnout.",
        "düşük bütçe": "Risk of unrealistic expectations given the budget.",
        "tüm özellikler": "Risk of an overly broad scope without clear prioritization.",
        "hemen başla": "Risk of insufficient planning and rushed start."
    }
    potential_risks = []
    for keyword, risk_desc in risk_indicators.items():
        if keyword in brief_text_lower:
            potential_risks.append(f"'{keyword}': {risk_desc}")
    
    # Heuristic for common time-related risk
    if "en kısa sürede" in brief_text_lower or "mümkün olan en kısa sürede" in brief_text_lower:
        potential_risks.append("'En kısa sürede' / 'Mümkün olan en kısa sürede': Implies a tight deadline, potential for rushed work and quality issues.")


    return {
        "identified_requirements": identified_requirements if identified_requirements else ["No specific requirements clearly identified."],
        "potential_ambiguities": potential_ambiguities if potential_ambiguities else ["No obvious vague terms found that require clarification."],
        "missing_information_questions": questions_to_ask if questions_to_ask else ["Brief seems comprehensive, but always good to confirm details."],
        "potential_risks": potential_risks if potential_risks else ["No immediate high-level risks detected."]
    }

if __name__ == "__main__":
    # Example Project Brief (in Turkish, as per article context)
    sample_brief = """
    Merhaba, yeni bir e-ticaret web sitesi projesi için teklif almak istiyorum.
    Sitemizin modern, hızlı ve kullanıcı dostu olması çok önemli.
    Müşterilerimiz kolayca ürünleri bulabilmeli ve satın alabilmeli.
    Ödeme sistemleri entegrasyonu ve bir yönetim paneli de gerekiyor.
    Projeyi mümkün olan en kısa sürede tamamlamak istiyoruz.
    Lütfen detaylı bir teklif ve zaman çizelgesi sunar mısınız?
    """

    print("--- ScopeNote Local AI Analysis Simulation ---")
    print("\nOriginal Brief:")
    print(sample_brief)
    print("-" * 50)

    # Perform the simulated local AI analysis
    analysis_results = analyze_brief_local_ai_mock(sample_brief)

    print("\nAnalysis Results:")
    print("\n1. Identified Requirements:")
    for req in analysis_results["identified_requirements"]:
        print(f"  - {req}")

    print("\n2. Potential Ambiguities / Vague Terms:")
    for ambiguity in analysis_results["potential_ambiguities"]:
        print(f"  - {ambiguity}")

    print("\n3. Missing Information / Questions to Ask:")
    for question in analysis_results["missing_information_questions"]:
        print(f"  - {question}")

    print("\n4. Potential Risks:")
    for risk in analysis_results["potential_risks"]:
        print(f"  - {risk}")

    print("\n--- End of Analysis ---")
