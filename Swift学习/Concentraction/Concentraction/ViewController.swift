//
//  ViewController.swift
//  Concentraction
//
//  Created by Lee Morales on 2019/5/3.
//  Copyright © 2019 Lee Morales. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    private lazy var game: Concentraction = Concentraction(numberOfPairsOfCards: numberOfPairsOfCards)
    
    var numberOfPairsOfCards: Int {
            return ((cardButtons.count+1) / 2)
    }
    
    private(set) var flipCount = 0 { didSet { flipCountLabel.text = "Flips: \(flipCount)" } }
    
    @IBOutlet private weak var flipCountLabel: UILabel!
    
    @IBOutlet private var cardButtons: [UIButton]!
    
    
    
    @IBAction private func touchCard(_ sender: UIButton) {
            flipCount += 1
        if let cardNumber = cardButtons.firstIndex(of:sender) {
                game.chooseCard(at: cardNumber)
                updateViewFromModel()
            }else{
                print("Choosen card was not in the cardbutton")
        }
    }
    
    private func updateViewFromModel() {
        for index in cardButtons.indices {
            let button = cardButtons[index]
            let card = game.cards[index]
            if card.isFaceUp {
                button.setTitle(emoji(for: card), for: UIControl.State.normal)
                button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
            }else{
                button.setTitle("", for:UIControl.State.normal)
                button.backgroundColor = card.isMatched ? #colorLiteral(red: 0.9506973624, green: 0.9854659438, blue: 0.9847254157, alpha: 0) : #colorLiteral(red: 1, green: 0.5763723254, blue: 0, alpha: 1)
            }
        }
    }
}
    private var emojiChoices = ["🎃","👻","😱","😈","☠️","💀","👽","🤖","🔨"]

    private var emoji = [Int:String]()

    private func emoji(for card: Card) -> String {
        if emoji [card.identifier] == nil, emojiChoices.count > 0 {
            emoji[card.identifier] = emojiChoices.remove(at:emojiChoices.count.arc4random)
            }
        return emoji [card.identifier] ?? "?"
    }

extension Int {
    var arc4random: Int {
        if self > 0 {
        return Int(arc4random_uniform(UInt32(self)))
        }else if self < 0 {
            return -Int(arc4random_uniform(UInt32(abs(self))))
        }else{
            return 0
        }
    }
}
