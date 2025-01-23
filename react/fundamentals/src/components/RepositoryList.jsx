import '../styles/global.scss'
import RepositoryItem from './RepositoryItem';

const repository1 = {
    name: 'Expression Calculator',
    description: '☕ Desktop Java Expression Calculator using Infix-to-Postfix Conversion with Linked List-based Stack and Queue 💻',
    link: 'https://github.com/ODCS1/Expression-Calculator'
}
const repository2 = {
    name: 'Page Rank',
    description: '🐍 Python desktop application for PageRank calculation using Markov Chains. Includes graphs 📊 and results for test HTML pages 🌐.',
    link: 'https://github.com/ODCS1/PageRank'
}
const repository3 = {
    name: 'Canteen Management',
    description: '🍕💻 Python app for canteen management: orders 📋, accounts 💳, and money credits 💸',
    link: 'https://github.com/ODCS1/Canteen-Management'
}
const repository4 = {
    name: 'Smart House',
    description: '☕ Smart house arduino project application',
    link: 'https://github.com/ODCS1/Smart-House'
}

export function RepositoryList() {
    return (
        <section className="repository-list">
            <h1>Repository List</h1>

            <ul>
                <RepositoryItem repository={repository1}/>
                <RepositoryItem repository={repository2}/>
                <RepositoryItem repository={repository3}/>
                <RepositoryItem repository={repository4}/>
            </ul>
        </section>
    );
}